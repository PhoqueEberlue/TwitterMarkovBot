import twitter

def getApi():
    return twitter.Api(consumer_key='YOURKEY',
                        consumer_secret='YOURKEY',
                        access_token_key='YOURKEY',
                        access_token_secret='YOURKEY',
                        tweet_mode='extended')