import discord
from discord.ext import commands
from dataclasses import dataclass
from typing import List
import asyncio
import json

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
            data = json.loads(f)

            for members in data['members']:
                if str(member.id) in members['user_id']:
                    pass

                else:
                    new_user = User('''new User instance''')
                    # data['members'].update(dict(user_id='member.id', jokes=[]))
                    data['members'].update(new_user.__dict__)
                    f.seek(0)
                    json.dump(data, f)
                    break

    @client.event
    async def on_reaction_add(reaction, user):

    @commands.command()
    async def list_favorites(self, ctx, *, member):


class Joke(commands.Cog):

    def __init__(self, bot):






class GuildData(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def get_guilds(self):

        users = get_users()

        for gulid in self.bot.guilds:
            for member in guild.members:

                with open("{}_{}.json".format(guild.name, guild.id), "r+") as f:
                    
                    for user in users:
                        json.dumps(user.__dict__)
                    #iterate through users array by calling get_users() and serialize it to json objects

    # @commands.Cog.listener()
    async def get_users(self):

        users = []
        for guild in self.bot.guilds:
            for member in guild.member:

                users.append(User(''' member info as param'''))

        return users

    #register commands for guild members for server status i guess


        

                

        



