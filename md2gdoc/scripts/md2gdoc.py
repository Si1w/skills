"""md2gdoc: sync a local Markdown file with a Google Doc via pandoc + Drive API.

push: pandoc converts the file body to .docx using the reference template,
      then uploads it as a Google Doc (create first time, update after);
      the Doc id is written back into the file's frontmatter.
pull: export the Doc as .docx, pandoc converts it back to Markdown,
      replacing the body and keeping frontmatter.
"""

import argparse
import io
import os
import shutil
import subprocess
import sys
from pathlib import Path

import frontmatter
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]
DOC_MIME = "application/vnd.google-apps.document"
DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
HOME = Path(os.environ.get("GDRIVE_HOME", Path.home() / ".config" / "gdrive"))
DOC_URL = "https://docs.google.com/document/d/{}/edit"
TEMPLATE = Path(__file__).resolve().parent.parent / "template" / "reference.docx"


def service():
    """Build an authenticated Drive client. First run opens a browser for consent."""
    creds_file = HOME / "credentials.json"
    token_file = HOME / "token.json"
    if not creds_file.exists():
        sys.exit(f"Missing {creds_file}. Run GCP setup first (see references/gcp-setup.md).")
    creds = Credentials.from_authorized_user_file(token_file, SCOPES) if token_file.exists() else None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                creds = None  # revoked or expired past recovery; re-consent below
        if not creds or not creds.valid:
            creds = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES).run_local_server(port=0)
        token_file.write_text(creds.to_json())
    return build("drive", "v3", credentials=creds)


def pandoc_bin():
    """Path to the pandoc binary: the one bundled with pypandoc, else PATH."""
    try:
        import pypandoc

        return pypandoc.get_pandoc_path()
    except (ImportError, OSError):
        pass
    if shutil.which("pandoc"):
        return "pandoc"
    sys.exit("pandoc not found: run `uv sync` (pypandoc-binary) or `brew install pandoc`.")


def pandoc(cmd, stdin=None):
    res = subprocess.run([pandoc_bin(), *cmd], input=stdin, capture_output=True)
    if res.returncode != 0:
        sys.exit(f"pandoc failed: {res.stderr.decode('utf-8', 'replace')}")
    return res.stdout


def strip_rules(content):
    """Drop horizontal rules (---, ***, ___ on their own line after a blank line).

    The blank-line guard keeps setext headings (`text` + `---`) and table rows intact.
    """
    import re

    return re.sub(r"(\n\s*\n)\s*(?:-{3,}|\*{3,}|_{3,})\s*(?=\n|\Z)", r"\1", content)


def md_to_docx(content, template, bib=None, csl=None, resource_dir=None):
    """Render the Markdown body to .docx bytes using the reference template.

    implicit_figures is disabled so images stay inline and their alt text is
    not rendered as a caption under the image.
    """
    if not Path(template).exists():
        sys.exit(f"Missing template {template}.")
    cmd = ["-f", "markdown-implicit_figures", "-t", "docx",
           "--reference-doc", str(template), "-o", "-"]
    if resource_dir:
        cmd += ["--resource-path", str(resource_dir)]
    if bib:
        cmd += ["--citeproc", "-M", "link-citations=true", "--bibliography", bib]
        if csl:
            cmd += ["--csl", csl]
    return pandoc(cmd, stdin=content.encode("utf-8"))


def docx_to_md(data):
    """Convert exported .docx bytes back to Markdown."""
    return pandoc(["-f", "docx", "-t", "gfm", "--wrap=none"], stdin=data).decode("utf-8")


def push(path, bib=None, csl=None, template=TEMPLATE):
    post = frontmatter.load(path)
    docx = md_to_docx(strip_rules(post.content), template, bib=bib, csl=csl,
                      resource_dir=Path(path).resolve().parent)
    media = MediaIoBaseUpload(io.BytesIO(docx), mimetype=DOCX_MIME)
    svc = service()
    gid = post.get("gdoc_id")
    if gid:
        svc.files().update(fileId=gid, media_body=media).execute()
        print("Updated " + DOC_URL.format(gid))
    else:
        title = post.get("title") or Path(path).stem
        created = svc.files().create(
            body={"name": title, "mimeType": DOC_MIME}, media_body=media, fields="id"
        ).execute()
        post["gdoc_id"] = created["id"]
        Path(path).write_text(frontmatter.dumps(post), encoding="utf-8")
        print("Created " + DOC_URL.format(created["id"]))


def pull(path):
    post = frontmatter.load(path)
    gid = post.get("gdoc_id")
    if not gid:
        sys.exit(f"No gdoc_id in {path}. Push it first, or add gdoc_id to the frontmatter.")
    data = service().files().export(fileId=gid, mimeType=DOCX_MIME).execute()
    post.content = docx_to_md(data)
    Path(path).write_text(frontmatter.dumps(post), encoding="utf-8")
    print(f"Pulled {gid} into {path}")


def main():
    ap = argparse.ArgumentParser(description="Sync a Markdown file with a Google Doc via pandoc docx.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("push")
    p.add_argument("file")
    p.add_argument("--bib", help="render [@key] citations against this .bib via pandoc --citeproc")
    p.add_argument("--csl", help="CSL style for --bib (default: pandoc's Chicago author-date)")
    p.add_argument("--template", default=TEMPLATE, help="reference .docx template (default: template/reference.docx)")
    sub.add_parser("pull").add_argument("file")
    args = ap.parse_args()
    if args.cmd == "push":
        push(args.file, bib=args.bib, csl=args.csl, template=args.template)
    else:
        pull(args.file)


if __name__ == "__main__":
    main()
