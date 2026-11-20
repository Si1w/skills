# AIRR access setup

## Choose the correct portal

Use [AIRRPortal](https://portal-airr.isambard.ac.uk/) for the AIRR award and membership. The Allocate Portal serves Bristol/GW4 awards. Project Leads manage AIRR membership in the award portal. See [Awards Portals](https://docs.isambard.ac.uk/user-documentation/guides/awards_portal/).

An application or award notification alone does not establish SSH access. Confirm the award is Active and the user is a member. If Pending, follow up with the Project Lead or allocator. The documented provisioning window starts after any embargo is lifted. See [Getting Started](https://docs.isambard.ac.uk/user-documentation/getting_started/).

Use [BriCS Portal](https://portal.isambard.ac.uk/) for access terms, UNIX username, and the resulting project. These are separate functions from award membership management. See [Portals overview](https://docs.isambard.ac.uk/user-documentation/information/portals/).

## Authenticate as an external university user

Choose University Login (MyAccessID) and the user's own institution, such as King's College London when applicable. AIRR is the allocation route, not an identity provider. Do not select Bristol or the BriCS administrator login merely because Bristol operates the facility.

The identity's email must match the award invitation. For an active award with an authorization error, compare the MyAccessID profile email with the invited email; the Project Lead must correct membership if they differ. Do not create another account as a workaround.

Use Other Login (IdP of last resort) only when the user's institution is unsupported or they lack a university account, and BriCS has provisioned that identity. Being external to Bristol is not sufficient reason to use it. Let the user complete sign-in, MFA, and acceptance of terms. For browser cookie problems, try a private window before changing browser settings. Source: [Setup](https://docs.isambard.ac.uk/user-documentation/tutorials/setup/).

## Set the UNIX username

In BriCS Portal, open the user menu, User Dashboard, then Edit. Set the UNIX username using 5 to 20 lowercase letters or digits, starting with a letter. The choice is permanent, so use the user's chosen name instead of deriving it from their local account. If an empty-short-name error persists after saving, sign out of both the portal and the [federated account](https://account.isambard.ac.uk/), then sign in again. Source: [UNIX username guide](https://docs.isambard.ac.uk/user-documentation/guides/shortname/).

## Prepare Clifton and SSH

Inspect `uname -s` and `uname -m` before choosing a binary. Follow the current [Clifton installation instructions](https://docs.isambard.ac.uk/user-documentation/guides/login/#install) and use official [release assets](https://github.com/isambard-sc/clifton/releases/latest). On macOS, distinguish Apple Silicon from Intel. Prefer an existing executable or a user-writable executable location over introducing a system-wide installation.

Reuse a supported existing SSH key. If none exists, create an Ed25519 key at an unused path; never overwrite an existing key. Use that path with Clifton's `--identity` option. Do not collect passwords, private keys, or MFA codes in chat. Return to the main skill's connection workflow after onboarding and installation.
