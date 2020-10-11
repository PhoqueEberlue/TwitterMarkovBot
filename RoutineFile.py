import json
from bot import Bot
from datetime import datetime, timedelta
from time import sleep


with open("TMBsettings.json", "r", encoding="utf-8") as read_file:
    settings = json.load(read_file)
bot = Bot(settings["UserId"], "data_tweets.json", "data_tweets_only_replies.json")


while True:
    waitingTime = 60*60*24
    with open("logs.json", "r", encoding="utf-8") as read_file:
        logs = json.load(read_file)
    try:
        bot.CollectingUsersTweets(True, 200)
        bot.StoringIntoJSON()
        # bot.AjustCoef()
        tweet = bot.GenerateTweet()
        while len(tweet) > 280:
            tweet = bot.GenerateTweet
        waitingTime = bot.getWaitingTime()
        postingHour = str(datetime.now() + timedelta(seconds=waitingTime))
        logs[str(datetime.now())] = {"tweet": tweet, "postingHour": postingHour, "waitingTime": waitingTime}
        # bot.PostTweet(tweet)
    except Exception as e:
        logs[datetime.now()] = {"exception": e}
    with open("logs.json", "w", encoding="utf-8") as write_file:
        json.dump(logs, write_file)
    sleep(waitingTime)
