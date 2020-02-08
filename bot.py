from MTG import Output
from random import randint
from config import getApi
import os
import json

api = getApi()


def occurencesRepliedUser(User):
    """
    this function is used to return the max of the repliedUsers dictionnary
    """
    return User["occurences"]


class Bot:
    def __init__(self, user, filename, repliesFilename):
        """
        user: The id of the user that you want to collect data from and that will be used in the app.
        filename: the name of the file that you want to store user's tweets (exluding replies) ex: "data_tweets.json". Please insert {} in this file otherwise it'll crash.
        repliesFilename: the name of the file that you want to store user's tweets (only replies to other users) ex: "data_replies.json". Please insert {} in this file otherwise it'll crash.
        """
        self._user = user
        self._stream = None
        self._filename = filename
        self._repliesFilename = repliesFilename
        self._repliedUsers = {}

    # SETTER
    def CollectingUsersTweets(self, noReplies, count):
        """
        Collects user's stream.
        noReplies: a boolean, True if you don't want replies, False if you want replies.
        count: a int between 1 and 200, this is the number of tweets that you want to load.
        Doesn't return anything.
        """
        self._stream = api.GetUserTimeline(user_id=self._user, screen_name='', since_id='', max_id='',
                                           count=count, include_rts=False, trim_user=True, exclude_replies=noReplies)

    def StoringIntoJSON(self):
        """
        Store user's stream (consider calling CollectingUsersTweets() before calling this one) into filename.
        Doesn't return anything.
        """
        with open(self._filename, "r", encoding="utf-8") as read_file:
            tweets = json.load(read_file)
        for post in self._stream:
            text = post.full_text
            filteredtext = ''
            link = False
            if str(post.id) not in tweets.keys():
                for i in range(len(text)):
                    if (len(text))-i >= 7:
                        if text[i] == 'h' and text[i+1] == 't' and text[i+2] == 't' and text[i+3] == 'p' and text[i+4] == 's' and text[i+5] == ':' and text[i+6] == '/' and text[i+7] == '/':
                            link = True
                    if not link:
                        if text[i] == '\n' and text[i-1] != '.' and text[i-1] != '!' and text[i-1] != '?' and text[i-1] != '\n':
                            filteredtext += '¶\n'
                        else:
                            filteredtext += text[i]
                    if link:
                        if text[i] == ' ' or text[i] == '\n':
                            link = False
                tweets[post.id] = {"text": filteredtext}
        with open(self._filename, "w", encoding="utf-8") as write_file:
            json.dump(tweets, write_file)

    def StoringIntoJSONOnlyReplies(self):
        """
        Store user's stream (consider calling CollectingUsersTweets() before calling this one) into filename.
        Doesn't return anything.
        """
        with open(self._repliesFilename, "r", encoding="utf-8") as read_file:
            tweets = json.load(read_file)
        for post in self._stream:
            text = post.full_text
            filteredtext = ''
            link = False
            mention = False
            if str(post.id) not in tweets.keys() and post.in_reply_to_user_id != self._user and post.in_reply_to_user_id != None:
                for i in range(len(text)):
                    if (len(text))-i >= 7:
                        if text[i] == 'h' and text[i+1] == 't' and text[i+2] == 't' and text[i+3] == 'p' and text[i+4] == 's' and text[i+5] == ':' and text[i+6] == '/' and text[i+7] == '/':
                            link = True
                    if text[i] == '@':
                        mention = True
                    if not link and not mention:
                        if text[i] == '\n' and text[i-1] != '.' and text[i-1] != '!' and text[i-1] != '?' and text[i-1] != '\n':
                            filteredtext += '¶\n'
                        else:
                            filteredtext += text[i]
                    if link:
                        if text[i] == ' ' or text[i] == '\n':
                            link = False
                    if mention:
                        if text[i] == ' ' or text[i] == '\n':
                            mention = False
                tweets[post.id] = {"text": filteredtext, "in_reply_to_user_id": str(
                    post.in_reply_to_user_id)}
        with open(self._repliesFilename, "w", encoding="utf-8") as write_file:
            json.dump(tweets, write_file)

    def updateUserRepliedDictionnary(self):
        """
        Update the dictionnary that contains the users that the user replied to.
        Doesn't return anything.
        """
        with open(self._repliesFilename, "r", encoding="utf-8") as read_file:
            tweets = json.load(read_file)
        res = {}
        for tweet in tweets:
            if tweets[tweet]['in_reply_to_user_id'] in res:
                res[tweets[tweet]['in_reply_to_user_id']]["occurences"] += 1
            else:
                res[tweets[tweet]['in_reply_to_user_id']] = {"occurences": 1}
        userToRemove = []
        for User in res.keys():
            if res[User]["occurences"] == 1:
                userToRemove.append(User)
        for User in userToRemove:
            res.pop(User)

        i = 0
        for User in res.keys():
            res[User]["screen_name"] = api.GetUser(User).screen_name
            os.system('cls' if os.name == 'nt' else 'clear')
            print("+" + "-"*100 + "+")
            print("|" + round(i/len(res)*100)*'█' + ((round(i/len(res)*100)-100)*-1)*' ' + '|')
            print("+" + "-"*100 + "+")
            print(str(round(i/len(res)*100)) + "%")
            i += 1
            
        self._repliedUsers = res

    # GETTER
    def CollectLastTweetFromUser(self, user):
        """
        user: the id of the user (int).
        return the tweet of the last user.
        """
        lastTweet = api.GetUserTimeline(user_id=user, screen_name='', since_id='', max_id='',
                                        count=1, include_rts=False, trim_user=True, exclude_replies=True)
        return lastTweet[0]

    def getMostFrequentUser(self):
        """
        return the user that the class user responded the most.
        """
        Id = max(set(self._repliedUsers), key=occurencesRepliedUser)
        User = api.GetUser(user_id=Id)
        return User

    def getRepliedUserDictionnary(self):
        """
        return the dictionnary that contains all users that has been replied by the user.
        """
        return self._repliedUsers

    def getUser(self, Id):
        """
        Id: the id of the user (int).
        return the user data.
        """
        return api.GetUser(user_id=Id)

    def GenerateTweet(self, filename, MaxSentences):
        """
        filename: the name of the file that you want to gather data ex:"data_tweets.json".
        MaxSententences: a int between 0 and infinite (you are limited to 140 char so putting 99999 musn't be a good idea).
        return a tweet generated by the Makov chain (str).
        """
        return Output(filename, randint(1, MaxSentences)).replace('¶', '')

    # POSTER
    def PostTweet(self, tweet):
        """
        tweet: str.
        post a tweet.
        """
        api.PostUpdate(tweet)

    def PostReply(self, tweet, tweetToReplyID):
        """
        tweet: a str with the @ of the user that you want to reply to at the beginning of the str.
        tweetToReply: tweet's id that you want to reply.
        post a reply to a tweet.
        """
        api.PostUpdate(tweet, in_reply_to_status_id=tweetToReplyID)
