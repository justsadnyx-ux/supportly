# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project mostly adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
