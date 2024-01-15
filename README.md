# ShareLink (discord.py)

## Setup
```bash
pip install -r requirements.txt
```

## Execution
```bash
python -m share_link
```

## Usage

### Commands
- `/share link <url:string>`: Share a link
- `/guild`: Guild settings
    - `/guild add`: Add current guild as available guild
    - `/guild remove`: Remove current guild from available guilds
- `/config`: User settings
    - `/config set_guild <guild_id:string>`: Set guild to share links
    - `/config remove`: Remove user profile

### Buttons

#### Database Buttons
If you try to share a link to an unknown Twitter account that isn't registered in the database, the bot will ask whether to register it in the database or display it as an alternative account.
- `Add ID`: Register the account in the database
- `Use Different ID`: Display the account as an alternative account

#### Alternative Account Selection Buttons
By pushing the `Use Different ID` button, the bot will display a list of alternative accounts.
- `USER_A`|`USER_B`|`USER_C`|`...`: Select the account name to share the link

> This feature is useful for grouping a photographer's posts by associating them with the subject's account.


### Message
You can also share links by sending a message to the bot.
This is an alternative to the `/share link <url:string>` command.

Currently, the bot can share links from the following sources:
- `https://twitter.com/.../status/...`: Share a tweet
- `https://x.com/.../status/...`: Share a tweet

Other links will be available soon.

