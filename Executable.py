import os
import json
from rich.console import Console
from rich.table import Column, Table
from bot import Bot

console = Console()
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

with open("TMBsettings.json", "r", encoding="utf-8") as read_file:
            settings = json.load(read_file)

#Configuration menu
def configurationMenu():
    clearConsole()
    settingsTable = Table(show_header=True, header_style="Green")
    settingsTable.add_column("Welcome to the twitter Markov bot")
    settingsTable.add_row("Please enter the ID of the account that you want to track")
    console.print(settingsTable)
    UserId = input()
    User = Bot.getUser(UserId)
    clearConsole()
    settingsTable = Table(show_header=True, header_style="Green")
    settingsTable.add_column("Is it the right account? Y/N")
    settingsTable.add_row("Name: " + User.name)
    settingsTable.add_row("Screen Name: " + "@" + User.screen_name)
    settingsTable.add_row("Followers: " + str(User.followers_count))
    settingsTable.add_row("Location: " + User.location )
    console.print(settingsTable)
    res = input()
    if res == "Y" or res == "y":
        settings["UserId"] = UserId
        settings["Name"] = User.name
        settings["Screen_Name"] = User.screen_name
        settings['Location'] = User.location
        with open("TMBsettings.json", "w", encoding="utf-8") as write_file:
            json.dump(settings, write_file)
    elif res == "N" or res == "n":
        pass

if settings["UserId"] == None:
    configurationMenu()




#Main menu
table = Table(show_header=True, header_style="Green")
table.add_column("Twitter Markov Bot")
table.add_row("1. Post a status")
table.add_row("2. Post a status with a keyword")
table.add_row("3. Reply to someone\'s last tweet")
table.add_row("4. update replied list")
table.add_row("5. update tweet stream")
table.add_row("6. refresh profile picture")
table.add_row("7. Quit")

bot = Bot(settings["UserId"], "data_tweets.json", "data_tweets_only_replies.json")

def menu1():
    entered = ''
    while entered != 'ok':
        clearConsole()
        tweet = bot.GenerateTweet("data_tweets.json", 2)
        tweetTable = Table(show_header=True, header_style="Green")
        tweetTable.add_column("Post a status")
        tweetTable.add_row(tweet)
        console.print(tweetTable)
        entered = input('Enter "ok" if the message seems good\n')
        if entered == "quit":
            return None
    bot.PostTweet(tweet)

def menu2():
    inData = False
    Key = ""
    while not inData:
        clearConsole()
        if Key == "":
            print("Enter a keyword")
        else:
            print("This keyword isn't in the data base")
        Key = input()
        inData = bot.isKeyInData(Key)
    entered = ''
    while entered != 'ok':
        clearConsole()
        tweet = bot.GenerateTweetWithKey("data_tweets.json", 2, Key)
        tweetTable = Table(show_header=True, header_style="Green")
        tweetTable.add_column("Post a status with key: " + Key)
        tweetTable.add_row(tweet)
        console.print(tweetTable)
        entered = input('Enter "ok" if the message seems good\n')
        if entered == "quit":
            return None
    bot.PostTweet(tweet)

def menu3():
    clearConsole()
    selectTable = Table(show_header=True, header_style="Green")
    selectTable.add_column("Select an user to reply")
    dictionnary = bot.getRepliedUserDictionnary()
    for User in dictionnary.keys():
        selectTable.add_row(dictionnary[User]["screen_name"])
    console.print(selectTable)
    userInDictionnary = False
    while not userInDictionnary:
        entered = input()
        for User in dictionnary.keys():
            if dictionnary[User]["screen_name"] == entered:
                UserToReplyId = User
                userInDictionnary = True
                break
            print("error: user not in dictionnary")
    LastTweet = bot.CollectLastTweetFromUser(UserToReplyId)
    entered = ''
    while entered != 'ok':
        clearConsole()
        tweet = "@" + dictionnary[UserToReplyId]["screen_name"] + " " + bot.GenerateTweet("data_tweets_only_replies.json", 1)
        print("---------------Type \"quit\" to quit----------------------")
        print(dictionnary[UserToReplyId]["screen_name"] + ": " + LastTweet.full_text)
        print("--------------------------------------------------------")
        print(tweet)
        print("--------------------------------------------------------")
        entered = input('Enter "ok" if the message seems good\n')
        if entered == "quit":
            return None
    bot.PostReply(tweet, LastTweet.id)

def menu6():
    bot.refreshPorfilePicture()
    
UserInput = ''
while UserInput != 'quit':
    clearConsole()
    console.print(table)
    UserInput = input()
    if UserInput == "1":
        menu1()
    if UserInput == "2":
        menu2()
    if UserInput == "3":
        menu3()
    if UserInput == "4":
        bot.updateUserRepliedDictionnary()
    if UserInput == "5":
        bot.CollectingUsersTweets(False, 200)
        bot.StoringIntoJSONOnlyReplies()
        bot.CollectingUsersTweets(True, 200)
        bot.StoringIntoJSON()
    if UserInput == "6":
        menu6()
    if UserInput == "7":
        UserInput = 'quit'