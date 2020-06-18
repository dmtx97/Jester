from ..lib import discord_imports
from ..user import User

class Server(commands.Cog):

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
            user = User(member.name, member.id, []).to_dict()
            users[discriminator] = user
        
        return users

def setup(bot):
    bot.add_cog(Server(bot))