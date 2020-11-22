import json
from bot import Bot
from datetime import datetime, timedelta
from time import sleep
from random import randint

with open("TMBsettings.json", "r", encoding="utf-8") as read_file:
    settings = json.load(read_file)
bot = Bot(settings["UserId"], "data_tweets.json", "data_tweets_only_replies.json")

sleep(0.01)
lastTweet = bot.CollectLastTweetFromSelf()
with open("logs.json", "r", encoding="utf-8") as read_file:
    logs = json.load(read_file)
if int(logs[list(logs)[-1]]["lastTweetFromUser"]) != lastTweet.id:
    sleep(0.01)
    print("yo")
    bot.CollectingUsersTweets(True, 200)
    bot.StoringIntoJSON()
    # bot.AjustCoef()
    tweet = bot.GenerateTweet()
    while len(tweet) > 280:
        tweet = bot.GenerateTweet()
    logs[str(datetime.now())] = {"tweet": tweet, "lastTweetFromUser": lastTweet.id}
    with open("logs.json", "w", encoding="utf-8") as write_file:
        json.dump(logs, write_file)
    sleep(randint(60,50*60))
    bot.PostTweet(tweet)

