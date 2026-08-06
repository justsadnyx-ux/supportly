# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project mostly adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

# v1.1.4

### Changed
* Verification release: confirms the fully automatic update pipeline works end to end on this deployment — the bot detects the newer version from the changelog, runs `git pull`, posts the changelog + "Bot has been updated" embed to `#our-bot-updates`, and restarts itself with no manual steps.

# v1.1.3

### Fixed
* Auto-update no longer hangs on local (non-Heroku) hosting. The GitHub fork-sync API call was running before `git pull` on every hosting method even though only Heroku uses it, and with no GitHub token configured it could block the check indefinitely — leaving the bot stuck on an older version with no notification and no restart. The API call is now skipped unless running on Heroku.

# v1.1.2

### Changed
* `?update` no longer replies in the channel where it's run. Results post **only** to the configured update channel (`#our-bot-updates`).

# v1.1.1

### Changed
* Auto-updates are now enabled by default on this deployment (`DISABLE_AUTOUPDATES=false`): the bot checks the changelog every 15 minutes and again shortly after every boot.
* When a newer version exists, the bot automatically runs `git pull`, posts the full changelog to `#our-bot-updates`, and restarts itself — no `?update` needed.
* Each check logs `Autoupdate check: current vX, latest vY` so the loop's activity is visible.

# v1.1.0

### Performance
* Messages are processed in a single pass: invocation contexts and the thread lookup are built once per message and reused for both moderator message-logging and command dispatch (previously the thread could be looked up 2–4 times and contexts parsed twice per message).
* Reaction emoji (`sent_emoji`/`blocked_emoji`) are resolved once and cached, invalidating automatically when their config values change; previously they were re-resolved on every DM and every reply.

### Fixed
* Fixed corrupted (double-encoded) emoji characters in the source that made the "queued command" reaction (`⏳`) and an unsnooze log message render as garbled text.

# v1.0.9

### Changed
* Docs site UI unified across `index.html`, `vps.html`, and a new `changelog.html`; shared `style.css` with copy-to-clipboard and smooth-scroll.
* Changelog rendered as styled version cards; latest release fetched live from the public GitHub Releases API (no token).
* `?update` is a read-only check (no pull/restart); posts the full latest changelog to `#our-bot-updates`.

### Added
* `docs/vps.html` VPS deployment guide (systemd unit, secrets via `/etc/default/supportly`).
* Optional public health-status badge on the homepage (configured via the `supportly-health-url` meta; off by default).

# v1.0.8

### Changed
* `?update` is now a read-only update *check*: it reports the current vs. latest version and posts the full latest changelog to `#our-bot-updates`, but no longer pulls or restarts the bot.
* GitHub Pages site (`docs/index.html`) refreshed with a hand-written design; docs still hosted on Pages (not the bot — the bot runs locally and reads its token from `.env`).

### Added
* `#our-bot-updates` (1533409707409018992) receives the full latest changelog embed on each `?update` check.

# v1.0.7

### Changed
* Test release for the update-notification + GitHub Pages changelog pipeline.

# v1.0.6

### Added
* `?about` now links to the support server, GitHub repo, and GitHub Pages site.

# v1.0.5

### Changed
* Changelog is served from the GitHub Pages site (https://justsadnyx-ux.github.io/supportly/).

# v1.0.4

### Changed
* Changelogs are no longer DM'd. The latest changelog is posted to the configured update channel (`#our-bot-updates`) on every release.
* Changelog source now points to the GitHub Pages site (`justsadnyx-ux.github.io/supportly`); only the latest version is published.

# v1.0.3

### Improved
* Update notifications are now also posted to the configured update channel when running `?update`.
* The update message now notes that the bot restarts automatically.

# v1.0.2

### Fixed
* Test release to verify the auto-update and changelog DM pipeline.

# v1.0.1

### Changed
* Removed typing indicators for instant replies.
* Changelogs are now DMed to the owner(s) and all server members whenever a new release is detected.

# v1.0.0

### Added
* **Supportly** — an independent Discord support bot, fully rebranded from its upstream origins.
* Premium gating: premium features require membership in the support server with the `Premium` role.
* Support server invitation: `https://discord.gg/25YRFavwpj`.
* Custom status: `DM - FOR SUPPORT`.

### Changed
* Version reset to `v1.0.0`.
* Plugin registry and changelog sources now point to the Supportly repository (`justsadnyx-ux/supportly`).
* Removed all third-party social media links and branding.
