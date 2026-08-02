<div align="center">
  <br>
  <strong><i>A feature-rich Supportly bot for Discord.</i></strong>
  <br>
  <br>

  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Made%20With-Python%203.10-blue.svg?style=for-the-badge&logo=Python" alt="Made with Python 3.10">
  </a>

  <a href="#">
    <img src="https://img.shields.io/badge/license-agpl-e74c3c.svg?style=for-the-badge" alt="AGPL License">
  </a>

<br>
</div>


## What is Supportly?

Supportly is a self-hosted Discord bot that serves as a shared inbox for server staff to communicate with their users in a seamless way. When a user DMs the bot, a support thread is created in your server where staff can reply, and the user's response is relayed back and forth.

## Features

- **Thread-based inbox** - each user contact becomes a support thread channel
- **Anonymous replies** - reply without revealing staff identity
- **Group conversations** - contact up to 5 users at once
- **Snippets** - save and reuse canned responses
- **Notes** - persistent notes on users, visible to staff
- **Logging** - message logs with links, transcript export
- **Permission levels** - granular control over who can do what
- **Plugins** - extend functionality with third-party plugins
- **Customization** - configurable responses, colors, emojis, and more

## Installation

1. Create a Discord application at the [Discord Developer Portal](https://discord.com/developers/applications)
2. Enable the **Message Content** privileged intent for your bot
3. Invite the bot to your server with the required permissions
4. Copy `.env.example` to `.env` and fill in your bot token and connection URI
5. Install dependencies: `pip install -r requirements.txt`
6. Run the bot: `python bot.py`
7. In your server, run `?setup` to configure the bot

> Requires a MongoDB connection URI (`CONNECTION_URI`) for data storage.

## License

This project is licensed under the **GNU Affero General Public License v3.0**. See [LICENSE](LICENSE) for details.
