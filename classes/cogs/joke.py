from ..lib import discord_imports

class Joke(commands.Cog):

    def __init__(self, bot):

    @commands.command()
    async def telljoke(self, ctx, *args):

        message = ""
        with open("redditJokes.json", "r+") as f:

            data = json.loads(f.read())

            joke_list = []
                for date in data:
                    for content in data[date]:

                        ran = random.randint(0, joke_len)
                        joke_list.append(content)
                        joke_len = len(content)

                        if len(args) > 0 and content["joke_id"] == args:
                            message += "```{} \n\n {} ``` \n Joke ID: {}".format(content["title"], content["text"], content["joke_id"])

                        else:
                            message += "```{} \n\n {} ``` \n Joke ID: {}".format(joke_list[ran]["title"], joke_list[ran]["text"], joke_list[ran]["joke_id"])

        await bot.send(message)

def setup(bot):
    bot.add_cog(Joke(bot))