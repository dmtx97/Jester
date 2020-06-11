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
    # user_discriminator : str
    jokes : List = []

class Member(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @bot.event()
    async def on_member_join(self, member):

        with open("guild_members.json", "r+") as f:
            data = json.loads(f.read())

            if member.discriminator in data:
                pass

            else:
                new_user = User(member.name, member.id, member.discriminator, [])
                data.update(new_user.to_dict())
                f.seek(0)
                json.dump(data, f, indent=4, sort_keys=False)

    @bot.event
    async def on_reaction_add(reaction, user):

        if(reaction.emoji == ⭐):

            with open("guild_members.json", "a+") as f:

                data = json.loads(f)

                if(user.discriminator in data):
                    date_added = datetime.today().strftime("%m/%d/%Y")
                    message = reaction.message.content 
                    joke_id = message.partition("Joke ID: ")[2]
                    # data[user.discriminator]['jokes'].append({'date_added' : date_added, 'joke_id' : joke_id})
                    data[user.discriminator]['jokes'].append(joke_id)
                    json.dump(data, f, indent=4, sort_keys=False)

    @commands.command()
    async def listfavs(self, ctx, *, member = discord.Member):

        embed = discord.Embed(
            title = "{}'s Saved Jokes".format(member.name)
            description = "Below is a preview of the jokes that you have saved. To view the full joke, use command !telljoke along with the joke ID seperated by a space"
            colour = purple
        )

        member_file = open("guild_members", "r")
        member_data = json.loads(member_file)
        jokes_file = open("guild_memmbers", "r")
        jokes_data = json.loads(jokes_file)
        dis = member.discriminator

        joke_ids = []
        if dis in jokes_data:
            for val in member_data[dis]:
                joke_ids + val['jokes']

                #loop and splice joke after 25 characters and replace with ... use a \n.join(string) to add new line 
                #do the same for the joke ID
                #possible for date added
                #create 
        
        '''possibly change id for the key for the json file instead of date and place the date aquired inside. this will reduce one for loop'''
        for date in jokes_data:
            for content in jokes_data[date]:
                for ids in joke_ids:

                    if content['joke_id'] == ids:

        #embed the fields = title, date added, and joke id

        #for each joke id in user, create dictionary 

class Joke(commands.Cog):

    def __init__(self, bot):

class GuildData(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_guild_join(guild):

        users = self.get_users(guild)

        with open("guild_members.json", "a+") as f:
            json.dumps(users, f, indent=4, sort_keys=False)

    @commands.Cog.listener()
    async def get_users(self, guild):

        users = {}
        for member in guild.members:
            discriminator = member.discriminator
            users[discriminator] = []
            users[discriminator].append(User(member.name, member.id, []).to_dict())
        
        return users

#create commands for server status