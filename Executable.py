from bot import Bot
import os

Narkuss = Bot(1502450814, "data_tweets.json", "data_tweets_only_replies.json")

def menu1():
    entered = ''
    while entered != 'ok':
        os.system('cls' if os.name == 'nt' else 'clear')
        tweet = Narkuss.GenerateTweet("data_tweets.json", 3)
        print("--------------------------------------------------------")
        print(tweet)
        print("--------------------------------------------------------")
        entered = input('Enter "ok" if the message seems good\n')
        if entered == "quit":
            return None
    Narkuss.PostTweet(tweet)

def menu2():
    print("---------------------------------------------------------------")
    print("Select an user to reply (Most frequent replied user is default)")
    print("---------------------------------------------------------------")
    dictionnary = Narkuss.getRepliedUserDictionnary()
    for User in dictionnary.keys():
        print(dictionnary[User]["screen_name"])
    userInDictionnary = False
    while not userInDictionnary:
        entered = input()
        if entered == "":
            UserToReplyId = Narkuss.getMostFrequentUser().id
            userInDictionnary = True
        else:
            for User in dictionnary.keys():
                if dictionnary[User]["screen_name"] == entered:
                    UserToReplyId = User
                    userInDictionnary = True
                    break
        print("error: user not in dictionnary")
    LastTweet = Narkuss.CollectLastTweetFromUser(UserToReplyId)
    entered = ''
    while entered != 'ok':
        os.system('cls' if os.name == 'nt' else 'clear')
        tweet = "@" + dictionnary[UserToReplyId]["screen_name"] + " " + Narkuss.GenerateTweet("data_tweets_only_replies.json", 1)
        print("---------------Type \"quit\" to quit----------------------")
        print(dictionnary[UserToReplyId]["screen_name"] + ": " + LastTweet.full_text)
        print("--------------------------------------------------------")
        print(tweet)
        print("--------------------------------------------------------")
        entered = input('Enter "ok" if the message seems good\n')
        if entered == "quit":
            return None
    Narkuss.PostReply(tweet, LastTweet.id)




UserInput = ''
while UserInput != 'quit':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('+---------------------------------------------+')
    print('| Welcome to the twitter Markov bot           |')
    print('+---------------------------------------------+')
    print('| 1. Post a status                            |')
    print('| 2. Reply to someone\'s last tweet            |')
    print('| 3. update replid list                       |')
    print('| 4. update tweet streeam                     |')
    print('| 5. Quit                                     |')
    print('+---------------------------------------------+')

    UserInput = input()
    if UserInput == "1":
        menu1()
    if UserInput == "2":
        menu2()
    if UserInput == "3":
        Narkuss.updateUserRepliedDictionnary()
    if UserInput == "4":
        Narkuss.CollectingUsersTweets(False, 200)
        Narkuss.StoringIntoJSONOnlyReplies()
        Narkuss.CollectingUsersTweets(True, 200)
        Narkuss.StoringIntoJSON()
    if UserInput == "5":
        UserInput = 'quit'