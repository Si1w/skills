# GCP setup (once)

Goal: a `credentials.json` for a Desktop OAuth client that can reach your Drive. Do this once at <https://console.cloud.google.com>. Menu labels vary by Console version; follow the intent of each step.

1. **Project**: create a project (or pick an existing one).
2. **Enable the API**: APIs & Services → Library → search "Google Drive API" → Enable.
3. **Consent screen** (old name OAuth consent screen, now called Google Auth Platform): go to APIs & Services → Google Auth Platform and click Get Started on first visit. In the Branding tab, enter the app name and your own email; in the Audience tab, set User type to External. Scopes live in the Data Access tab and can be skipped (the script requests the permission at authorization time); to add it explicitly, paste `https://www.googleapis.com/auth/drive` under "Manually add scopes".
4. **Publish**: in the Audience tab, set Publishing status to In production (Publish app); the app stays unverified, which only adds a one-time warning you click past, it does not block personal use. If you instead leave it in Testing, you must add your Google account under Test users on the same page or consent is refused outright, and the refresh token expires every 7 days.
5. **Create credentials**: APIs & Services → Credentials → Create Credentials → OAuth client ID → Application type Desktop app → any Name → Create → download JSON. The generated Client ID and secret are already inside the downloaded JSON; nothing to fill in by hand.
6. **Place it**: rename the file to `credentials.json` and move it to `~/.config/gdrive/credentials.json`.

First `push`/`pull` opens a browser: pick your account → on the "unverified" screen click Advanced → Continue → Allow. `token.json` is then written next to `credentials.json` and reused.

Scope requested by the script: `https://www.googleapis.com/auth/drive` (full Drive, so it can adopt Docs you did not create).
