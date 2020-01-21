from config import getApi
from MTG import Output
from random import randint
import os

api = getApi()


def postStatus(tweet):
    api.PostUpdate(tweet)


def CollectingTweets(user):
    stream = api.GetUserTimeline(user_id=user, screen_name='', since_id='', max_id='',
                                 count=200, include_rts=False, trim_user=True, exclude_replies=True)
    File = open('Data.txt', 'w',
                encoding="utf-8")
    for post in stream:
        text = post.text
        filteredtext = ''
        link = False
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
        File.write(filteredtext + '\n')
    File.write('\n')
    File.close()


CollectingTweets(1502450814) #The twitter ID of the account that you want to gather tweet
entered = ''
while entered != 'ok':
    res = Output('Data.txt', randint(1, 3)).replace('¶', '')   
    print(res)
    entered = input('Enter "ok" if the message seems good\n')

postStatus(res)