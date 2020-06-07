import discord
import asyncio
from bot import *

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!jokeme'):

        with open('redditJokes.json') as f:
            info = json.load(f)

        try:
            #determine lenght of items in json file
            json_len = len(info['jokes'])
            # generating random interger that is between
            # 0 and the lenght of items in the json file.
            x = random.randint(0,json_len-1)
            # print the results with spaces in between for neatness
            post_title = info['jokes'][x]['r/jokes']['title']
            post_text = info['jokes'][x]['r/jokes']['text']

            # post_link = info['jokes'][x]['r/jokes']['link']

            output = post_title + '\n \n' + post_text + '\n' + post_link

            await client.send_message(message.channel, output)

        except (IndexError,KeyError):
            print("oops no jokes were found...")



client.run('token')
