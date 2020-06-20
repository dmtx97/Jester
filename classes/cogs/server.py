import discord
from discord.ext import commands
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
from typing import List
import random
import asyncio
import json
from ..user import User

class Server(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        users = self.get_users(guild)

        with open("guild_members.json", "a+") as f:
            json.dump(users, f, indent=4, sort_keys=False)

    def get_users(self, guild):

        users = {}
        for member in guild.members:
            discriminator = member.discriminator
            user = User(member.name, member.id, []).to_dict()
            users[discriminator] = user
        
        return users

def setup(bot):
    bot.add_cog(Server(bot))