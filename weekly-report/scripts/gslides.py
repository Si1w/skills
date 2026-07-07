"""gslides.py: sync weekly-report.pptx with a Google Slides presentation.

push: upload the pptx to Drive as Google Slides (create the first time, then
      update the same presentation). The presentation id is stored next to the
      pptx in <name>.gslides.json.
pull: export the Google Slides presentation back to the local pptx.

Auth: OAuth client in ~/.config/gdrive/credentials.json
(see weekly-report/references/gcp-setup.md); token cached in token.json.
"""

import argparse
import io
import json
import os
import sys
from pathlib import Path

from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive"]
SLIDES_MIME = "application/vnd.google-apps.presentation"
PPTX_MIME = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
HOME = Path(os.environ.get("GDRIVE_HOME", Path.home() / ".config" / "gdrive"))
URL = "https://docs.google.com/presentation/d/{}/edit"


def service():
    creds_file = HOME / "credentials.json"
    token_file = HOME / "token.json"
    if not creds_file.exists():
        sys.exit(f"Missing {creds_file}. Run GCP setup first (see weekly-report/references/gcp-setup.md).")
    creds = Credentials.from_authorized_user_file(token_file, SCOPES) if token_file.exists() else None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                creds = None
        if not creds or not creds.valid:
            creds = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES).run_local_server(port=0)
        token_file.write_text(creds.to_json())
    return build("drive", "v3", credentials=creds)


def push(drive, pptx, state_file):
    media = MediaFileUpload(pptx, mimetype=PPTX_MIME)
    state = json.loads(state_file.read_text()) if state_file.exists() else {}
    if state.get("id"):
        drive.files().update(fileId=state["id"], media_body=media).execute()
    else:
        meta = {"name": pptx.stem, "mimeType": SLIDES_MIME}
        state["id"] = drive.files().create(body=meta, media_body=media, fields="id").execute()["id"]
        state_file.write_text(json.dumps(state))
    print(URL.format(state["id"]))


def pull(drive, pptx, state_file):
    if not state_file.exists():
        sys.exit("No linked presentation. Push first.")
    file_id = json.loads(state_file.read_text())["id"]
    request = drive.files().export_media(fileId=file_id, mimeType=PPTX_MIME)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    pptx.write_bytes(buf.getvalue())
    print(f"Pulled {pptx}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["push", "pull"])
    default_pptx = Path(__file__).parent.parent / "weekly-report.pptx"
    ap.add_argument("pptx", nargs="?", default=str(default_pptx))
    args = ap.parse_args()
    pptx = Path(args.pptx)
    state_file = pptx.with_suffix(".gslides.json")
    drive = service()
    (push if args.cmd == "push" else pull)(drive, pptx, state_file)


if __name__ == "__main__":
    main()
