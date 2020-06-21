import praw
import json
import os
import asyncio
import random
from datetime import datetime

class RedBot:

    def __init__(self, client_id, client_secret, user_agent, username, password):

        self.reddit = praw.Reddit(client_id = client_id,
                                  client_secret = client_secret,
                                  user_agent = user_agent,
                                  username = username,
                                  password = password)

        self.reddit.config.decode_html_entities = True

    def enumerate_jokes(self):

        with open('redditJokes.json', 'r+') as f:

            data = json.loads(f.read())
            i = 0

            for date in data:
                for content in data[date]:
                    i+=1
                    content['joke_id'] = i
            f.seek(0)
            json.dump(data, f, indent=4, sort_keys=False)

    def getJokes(self):
        today = datetime.today().strftime("%m/%d/%Y")
        jokes = {today: []}

        for submission in self.reddit.subreddit('jokes').hot(limit=200):
            post = self.reddit.submission(id=submission.id)
            title = post.title 
            text = post.selftext

            if post.score >= 100 and not post.edited and not post.stickied:
                jokes[today].append({'title': title, 'text' : text})

        return jokes

    def dumpJokes(self):

        jokes = self.getJokes()
        
        if os.path.isfile('redditJokes.json'):
            with open("redditJokes.json", "r+") as f:
                data = json.loads(f.read())
                data.update(jokes)
                f.seek(0)
                json.dump(data, f, indent=4, sort_keys = False)

        else:
            with open("redditJokes.json", "w+") as f:
                json.dump(jokes, f, indent=4, sort_keys = False)

        self.enumerate_jokes()

    def parseJson(self):

        with open("redditJokes.json", "r+") as f:

            data = json.loads(f.read())

            message = ""
            joke_list = []
            for date in data:
                for content in data[date]:

                    joke_list.append(content)

                    #ISSUE "Cannot send an empty message"
                    if content["joke_id"] == 14:
                        message += "```{}{} ``` \n Joke ID: {}".format(content["title"], content["text"], content["joke_id"])
                        break
            

            print(message)
        # test_dict = {"dan" : {"username" : "nacdan", "user_id" : 123, "jokes" : [{"joke_id" : "1", "joke_preview" : "preview"}, {"joke_id" : "2", "joke_preview" : "preview"},{"joke_id" : "3", "joke_preview" : "preview"}]}}


        # for content in test_dict["dan"]["jokes"]:

        #     if "1" in content.values():
        #         test_dict["dan"]["jokes"].remove(content)
        # print(test_dict)


        # print(test_dict)

        # with open('redditJokes.json', 'r+') as f:
        #     data = json.loads(f.read())
        #     joke_len = 0
        #     joke_list = []

        #     for date in data:
        #         for content in data[date]:
        #             joke_list.append(content)
        #             joke_len = len(content)
                    
        #     ran = random.randint(0, joke_len)
        #     print(joke_list[ran]["title"])