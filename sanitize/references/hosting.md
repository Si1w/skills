# Package and host an anonymous artifact

Use the venue's current artifact and anonymity requirements and verify the chosen service's current review-link behavior. Provider features can change; do not assume a private source or an unpublished record is accessible to reviewers.

## Code hosting

For Anonymous GitHub, check the current workflow at <https://anonymous.4open.science>. If it proxies a GitHub source repository, create fresh history from the verified copy using an anonymous commit identity. Use a neutral repository name, exclude the local sanitizer report, and check that the review link does not expose the source account, original URL, or author metadata. Never publish the original history.

Only create or push the remote when the requested destination and scope are authorized. Test the resulting review link as a reviewer would access it. Later fixes must pass the same sanitization and review process before updating the hosted copy.

## Archive hosting

For Zenodo or another archive, package the verified directory without `.git`, `.DS_Store`, or the sanitizer report. Inspect archive entries before uploading. Use anonymous author metadata without ORCID or affiliation, and check the venue's requirements for a DOI or review link. Publishing an archival record can be permanent; prepare a draft unless publication is requested or already authorized.

## Datasets and weights

Host newly produced large datasets, checkpoints, and traces separately when the artifact needs them. HuggingFace under a fresh anonymous organization is an option, subject to venue rules and data-release permissions. Inspect cards and embedded metadata for identifying content, and verify reviewer access. Cite reused datasets and models at their original sources instead of re-uploading them.

After acceptance, update the paper to point to the real repository. Plan any dataset or model ownership transfer using the service's current instructions and verify that links still resolve; do not assume transfer support or de-anonymize the review copy automatically.
