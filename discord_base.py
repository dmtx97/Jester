from config import *
import discord
from discord.ext import commands
from classes.discbot import DiscCog, Users


if __name__ == "__main__":

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                description='Joke Bot!')

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')


bot.add_cog(DisCog(bot))

bot.loop.create_task(get_guilds())
bot.run(discord_token)