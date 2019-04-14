import asyncio as asyncio
import discord
from discord import Game, Server, Member, Embed, Color
import configparser, os

from commands import cmd_ping, cmd_wtb, cmd_wts, cmd_market, cmd_help, cmd_clear

class DiscordOrderbookBot(object):
    commands = {
        "ping": cmd_ping,
        "wtb": cmd_wtb,
        "wts": cmd_wts,
        "market": cmd_market,
        "help": cmd_help,
        "clear": cmd_clear
    }

    def __init__(self):
        self.client = discord.Client()
        self.client.on_ready = self.on_ready
        self.client.on_message = self.on_message
        self.config = configparser.ConfigParser()
        self.config.read('bot.conf')

    def run(self):
        if not 'token' in self.config['secrets'] or not self.config['secrets']['token']:
            print('DiscordOrderbookBot: Value for "token" configuration option not found, please edit your bot.conf')
            return

        self.client.run(self.config['secrets']['token'])

    @asyncio.coroutine
    def on_ready(self):
        print("Bot is logged in succesfully. Running on servers: \n")
        for s in self.client.servers:
            print(" - %s (%s)" % (s.name, s.id))
        yield from self.client.change_presence(game=Game(name="Mesh"))

    @asyncio.coroutine
    def on_message(self, message):
        # print(message.content + " - " + message.author.name)
        if message.content.startswith(self.config['bot']['prefix']):
            # support channel ids and channel names as well (and long line format as for PEP8)
            if (message.server and 'auth_channels' in self.config['bot']     # when commented out in config, listen on all channels
                    and message.channel.id not in self.config['bot']['auth_channels'].split('\n')   # support multi-line values
                    and message.channel.name not in self.config['bot']['auth_channels'].split('\n')
                    ): 
                print('Unsupported channel: %s (%i)'.format(message.channel.name, message.channel.id))
                return
            
            sender = str(message.author)
            invoke = message.content[len(self.config['bot']['prefix']):].split(" ")[0]
            invoke = invoke.lower()
            args = message.content.split(" ")[1:]
            print("INVOKE: %s\nARGS: %s" % (invoke, args.__str__()[1:-1].replace("'","")))

            if self.commands.__contains__(invoke):
                yield from self.commands.get(invoke).ex(args, message, self.client, invoke, sender, self.config)
            else:
                yield from self.client.send_message(message.channel, embed=Embed(color=Color.red(), description=("The command '%s' is not valid." % invoke)))
                #to send a message to the author directly: yield from client.send_message(message.author, embed=Embed(color=Color.red(), description=("The command '%s' is not valid." % invoke)))

def main():
    app = DiscordOrderbookBot()
    app.run()

if __name__=='__main__':
    main()
