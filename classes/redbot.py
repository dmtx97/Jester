import praw
import json
import os
from datetime import datetime

class RedBot:

    def __init__(self, client_id, client_secret, user_agent, username, password):

        self.reddit = praw.Reddit(client_id = client_id,
                                  client_secret = client_secret,
                                  user_agent = user_agent,
                                  username = username,
                                  password = password)

        self.reddit.config.decode_html_entities = True

    def getJokes(self):

        today = datetime.today().strftime('%Y-%m-%d')
        today = datetime.today().strftime("%m/%d/%Y, %H:%M:%S")
        jokes = {'jokes' : [{today:[]}]}


        if not os.path.isfile('redditJokes.json'):
            with open("redditJokes.json", "a+") as f:
                json.dump(jokes, f, indent=4, sort_keys = False)

        with open("redditJokes.json", "r+") as f:
            data = json.loads(f.read())

            day_len = len(data["jokes"])

            # print(data["jokes"][day_len][today])

            for submission in self.reddit.subreddit('jokes').hot(limit = 20):

                post = self.reddit.submission(id=submission.id)
                title = post.title 
                text = post.selftext

            if post.score >= 300 and not post.edited and not post.stickied:
                data['jokes'][0][today].append(
                    {
                    'title' : title,
                    'text' : text,
                    }
                )

                data.update(data['jokes'])
                f.seek(0)
                json.dump(data, f, indent=4, sort_keys = False)

        # with open("redditJokes.json", "r+") as f:


        # for submission in self.reddit.subreddit('jokes').hot(limit = 20):
        #     post = self.reddit.submission(id=submission.id)
        #     title = post.title 
        #     text = post.selftext

        #     if post.score >= 300 and not post.edited and not post.stickied:
        #         jokes['jokes'][][today].append(
        #             {
        #             'title' : title,
        #             'text' : text,
        #             }
        #         )

        # if os.path.isfile('redditJokes.json'):

        #     with open("redditJokes.json", "r+") as f:
        #         data = json.loads(f.read())
        #         data.update(jokes['jokes'])
        #         f.seek(0)
        #         json.dump(data, f, indent=4, sort_keys = False)
                
        # else:

        #     with open("redditJokes.json", "w+") as f:
        #         json.dump(jokes, f, indent=4, sort_keys = False)


"""
To save jokes per user:

!jokeme will print out a random joke and react to it with a star:
when a user reacts to a message, it call the SaveJoke function and update the SavedUser JSON array. 
I will auto increment the saved jokes so when they type !listsaved, it will display the id along with the first sentence of the joke that was saved

schedule a function to append new user to SavedUser json array when they join the discord server:
this JSON file will contain an array of saved jokes per user...



"""
