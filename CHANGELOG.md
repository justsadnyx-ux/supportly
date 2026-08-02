# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project mostly adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

# v4.2.1

### Added
* `unsnooze_history_limit`: Limits the number of messages replayed when unsnoozing (genesis message and notes are always shown).
* Premium gating: premium features now require membership in the support server with the `Premium` role.
* Support server invitation: `https://discord.gg/25YRFavwpj`.
* Removed all third-party social media links and branding.

### Changed
* Project fully rebranded from the upstream name to **Supportly**.
* Plugin registry and changelog sources now point to the Supportly repository.
* The `oauth` (logviewer) premium feature is now gated by the premium check.
