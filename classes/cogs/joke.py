import discord
from discord.ext import commands
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
from typing import List
import random
import asyncio
import json

class Joke(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def telljoke(self, ctx, *args):

        message = " "
        with open("redditJokes.json", "r+") as f:

            data = json.loads(f.read())

            joke_list = []
            for date in data:
                for content in data[date]:

                    joke_list.append(content)

                    if len(args) > 0:

                        try:

                            if content["joke_id"] == int(args[0]):
                                message += "```{}\n{} ```Joke ID: {}".format(content["title"], content["text"], content["joke_id"])
                                break         

                            else:
                                message += "Joke ID Not Found"
                                break

                        except ValueError:
                            message += "Invalid Joke ID"
                            break           

            if len(args) == 0:

                joke_len = len(joke_list)
                ran = random.randint(0, joke_len)
                message += "```{}\n{}```Joke ID: {}".format(joke_list[ran]["title"], joke_list[ran]["text"], joke_list[ran]["joke_id"])
                
        # TODO: bot reacts to message with ⭐
        await ctx.send(message)
        # print(message)

def setup(bot):
    bot.add_cog(Joke(bot))