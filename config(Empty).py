import twitter

def getApi():
    return twitter.Api(consumer_key='YourKey',
                        consumer_secret='YourKey',
                        access_token_key='YourKey',
                        access_token_secret='YourKey',
                        tweet_mode='extended') #tweet_mode extended let us get the whole content of tweets