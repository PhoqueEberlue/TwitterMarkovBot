import json
from bot import Bot

with open("TMBsettings.json", "r", encoding="utf-8") as read_file:
            settings = json.load(read_file)

bot = Bot(settings["UserId"], "data_tweets.json", "data_tweets_only_replies.json")


while True:
    print(bot.GenerateTweet())
    input()