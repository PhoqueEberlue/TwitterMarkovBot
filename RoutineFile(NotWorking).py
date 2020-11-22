import json
from bot import Bot
from datetime import datetime, timedelta
from time import sleep


with open("TMBsettings.json", "r", encoding="utf-8") as read_file:
    settings = json.load(read_file)
bot = Bot(settings["UserId"], "data_tweets.json", "data_tweets_only_replies.json")


while True:
    with open("TMBsettings.json", "r", encoding="utf-8") as read_file:
        settings = json.load(read_file)
    bot = Bot(settings["UserId"], "data_tweets.json", "data_tweets_only_replies.json")
    sleep(1)
    lastTweet = bot.CollectLastTweetFromSelf()
    waitingTime = 60*60
    with open("logs.json", "r", encoding="utf-8") as read_file:
        logs = json.load(read_file)
    if int(logs[list(logs)[-1]]["lastTweetFromUser"]) != lastTweet.id:
        try:
            sleep(1)
            bot.CollectingUsersTweets(True, 200)
            bot.StoringIntoJSON()
            bot.AjustCoef()
            tweet = bot.GenerateTweet()
            while len(tweet) > 280:
                tweet = bot.GenerateTweet()
            waitingTime = bot.getWaitingTime()
            postingHour = str(datetime.now() + timedelta(seconds=waitingTime))
            logs[str(datetime.now())] = {"tweet": tweet, "postingHour": postingHour, "waitingTime": waitingTime, "lastTweetFromUser": lastTweet.id}
            with open("logs.json", "w", encoding="utf-8") as write_file:
                json.dump(logs, write_file)
            sleep(waitingTime)
            bot.PostTweet(tweet)
        except Exception as e:
            logs[str(datetime.now())] = {"Except": e}
            with open("logs.json", "w", encoding="utf-8") as write_file:
                json.dump(logs, write_file)
    else:
        sleep(waitingTime)
