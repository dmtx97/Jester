from classes.redbot import RedBot
from config import *
import praw
import asyncio

if __name__ == "__main__":
    joke = RedBot(client_id, client_secret, user_agent, username, password)
    joke.dumpJokes()
    # joke.parseJson()
    