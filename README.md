# Discord Orderbook bot
The discord orderbook bot, originally made for the Nyzo project.

Can be used for any type of discord channel where an orderbook bot is necessary.
Uses the discord.py library.

## Install

Needs python3

- Update SECRETS.py and STATICS.py to get started.
- Install requirements `pip3 install -r requirements.txt`
- run main.py `python3 main.py`

Some supervisor or cron helper could be needed to restart the bot should it crash.

## History

14/04/2019 - First Veles Core fork
- added support for standard ini-style config file
- refactored main script into class for better OOP

01/02/2019 - Bismuth version Public release
- removes some hardcoded Nyzo strings
- limit commands to specific channels only
- add WTS total and WTB Total
- clean up repo with .gitignore
- add requirements.txt
