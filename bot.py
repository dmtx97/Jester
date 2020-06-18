from config import *
import discord
from discord.ext import commands
import os

if __name__ == "__main__":

    bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                    description='Joke Bot!')

    @bot.event
    async def on_ready():
        print('Logged in as {0} ({0.id})'.format(bot.user))
        print('------')


    @bot.command()
    async def load(ctx, extension):
        bot.load_extension(f'classes.cogs.{extension}')

    @bot.command()
    async def unload(ctx, extension):
        bot.unload_extension(f'classes.cogs.{extension}')

    for filename in os.listdir('./classes/cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'classes.cogs.{filename[:-3]}')

    bot.run(discord_token)