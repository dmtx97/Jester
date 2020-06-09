import discord
from discord.ext import commands
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
from typing import List
import asyncio
import json

@dataclass_json
@dataclass
class User:
    '''Class for creating new users'''
    user_name : str
    user_id : int
    user_discriminator : str
    jokes : List = []

class Member(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
                                   #object of type Member 

        with open("users.json", "r+") as f:
            data = json.loads(f.read())

            for members in data['members']:
                if member.discriminator in members:
                    pass

                else:
                    new_user = User(member.name, member.id, member.discriminator, [])
                    data.update(new_user.to_dict())
                    json.dumps(data, f, indent=4, sort_keys=False)

                    f.seek(0)
                    json.dump(data, f)
                    break

    @bot.event
    async def on_reaction_add(reaction, user):

        if(reaction.emoji == ⭐):

            with open("guild_members.json", "a+") as f:

                data = json.loads(f)

                if(user.discriminator in data):
                    temp = data[user.discriminator]["jokes"]
                    date_added = datetime.today().strftime("%m/%d/%Y")
                    message = reaction.message.content 
                    joke_id = message.partition("Joke ID: ")[2]

                    # temp.append([{"date_added" : date_added},{"joke_id" : joke_id}])
                    temp.append([joke_id])

                    #dump




    @commands.command()
    async def listfavs(self, ctx, *, member):


class Joke(commands.Cog):

    def __init__(self, bot):

class GuildData(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def get_guilds(self):

        with open("guild_members.json", "a+") as f: 

            users = self.get_users()
            discriminator = [user.user_discriminator for user in users]

            for dis in discriminator:
                user_json = { dis : []}

                for user in users:
                    json.dumps(user_json[dis].append(user.to_dict()), f, indent=4, sort_keys=False)

    # @commands.Cog.listener()
    async def get_users(self):

        users = []
        for guild in self.bot.guilds:
            for member in guild.member:
                users.append(User(member.name, member.id, member.discriminator, []))

        return users

    #register commands for guild members for server status i guess


        

                

        



