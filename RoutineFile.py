import json
import datetime
from bot import Bot

with open("TMBsettings.json", "r", encoding="utf-8") as read_file:
            settings = json.load(read_file)

bot = Bot(settings["UserId"], "data_tweets.json", "data_tweets_only_replies.json")


while True:
    try:
        bot.CollectingUsersTweets(True, 200)
        bot.StoringIntoJSON()
        #bot.AjustCoef()
        tweet = bot.GenerateTweet()
        print(tweet)
        while len(tweet) > 280:
            tweet = bot.GenerateTweet
        print(datetime.datetime.now().hour)
        input()
        #bot.PostTweet(tweet)    
    except Exception as e:
        pass
     
    