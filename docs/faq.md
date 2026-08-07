# FAQ

## How do I contact support?
The bot's presence says `DM - FOR SUPPORT` — that is its actual Discord status, not a description. To start a conversation, DM the bot. Your first message opens a private thread in the support server, and staff reply back to you there.

## Why do releases post to #our-bot-updates?
That is the configured update channel for this bot. Every release — whether triggered manually by `?update` or by the automatic updater — posts the latest changelog there instead of DMing everyone. The bot never DMs server members on a new release.

(Before v1.0.4 the bot did DM changelogs on release. We stopped doing that.)

## What does ?update do?
It is a read-only check now. It compares the running version against the latest changelog, posts that changelog to `#our-bot-updates`, and reports it in chat if you have permission. It does **not** pull code or restart the bot, and it does not announce anything in the channel where you typed it — the result only goes to the update channel.

## Are updates automatic?
Yes. On this deployment the bot checks for a newer version every 15 minutes and once shortly after boot. When it finds one it:

1. runs `git pull` on its own working tree,
2. posts the changelog plus a "Bot has been updated" embed to `#our-bot-updates`,
3. logs `Bot has been updated.` and `Sent latest changelog to ...`,
4. logs out, and
5. the supervisor process restarts it on the new version.

One thing the bot owner should know: the graceful logout (`bot.close()`) on Windows can take a bit of time to actually tear the process down, so there is a short window on each update where the bot is briefly unavailable before the restart finishes. The new process comes back on its own — no manual restart needed.

## Why did the bot "hang" on v1.1.1?
The update check used to call the GitHub fork-sync API before `git pull`, even on hosts that do not use Heroku (where that call matters). With no GitHub token configured that API call could block indefinitely on a rate-limited endpoint, and the bot would get stuck showing the old version forever — no notification, no restart. **v1.1.3** skips the API call entirely unless the bot is running on Heroku. If you are on v1.1.3 or newer, you will not see this.

## Can I run Supportly myself?
Yes — it runs anywhere with Python 3.11, a MongoDB connection, and a Discord bot token. A VPS, a home server, or a Windows VM all work. See the [VPS guide](vps.html). GitHub Pages only hosts these docs; it cannot run the bot.

## How does premium work?
Some features are gated behind the `Premium` role in the support server. The bot checks for that role at runtime, so a member keeps access as long as they hold the role — no separate license key.

## Can I self-host on Heroku?
If you do, set a `github_token` variable. The auto-updater uses it to sync the fork, and without it the bot disables auto-updates on Heroku rather than failing. Everywhere else (local, VPS, PM2, systemd, Docker), auto-updates work without any token.

## The supportly-health-url meta tag — what's that?
A meta tag on `index.html`. If you expose a public `/health` endpoint on your own host, paste its URL there and the homepage shows a live online/offline dot. Leave it empty (current default) and the badge stays hidden. No secrets are ever stored client-side; the badge only hits the endpoint you specify.

## Is this the "real" Supportly?
Yes. This is the independent Supportly bot at `justsadnyx-ux/supportly`. The docs site lives at https://justsadnyx-ux.github.io/supportly/. It is open source under the AGPL v3.0.
