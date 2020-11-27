# Welcome to the TwitterMarkovBot page!
## What is it?
TwitterMakovBot is a Twitter bot that mimic the tweets of a given Twitter user using the [Markov chain](https://en.wikipedia.org/wiki/Markov_chain) principle.
For this example I'll mimic [@NarkussLol](https://twitter.com/NarkussLol) with an account called [@NarkussBot](https://twitter.com/NarkussBot).

## How does it work?
Firstly the bot stores all of the last tweets from the user in a JSON. Then it will be able to create new tweets that will look like the users one by using the Markov Chain.

![simple example of the markov chain](https://github.com/PhoqueEberlue/TwitterMarkovBot/blob/master/gitimages/simpleexample.png)

As you can see it is simply constructing sentences of "chains" of 2 words, but it is also using the probabilities, for exmple if "maths" had been used 2 times after "the", the chain would contain:
        
    {... 'the': {'maths':2, 'programmation':1}, ...}
Then maths would have a lot more chances to be constructed after "the".

## Setup

There is 2 ways of using this bot: 
-   Posting tweets generated by the bot by directly selecting them
-   Running the bot on a machine and letting the bot post by itself

### Installing

-   First you'll have to fork/download this projet
-   Create a new [twitter developper](https://developer.twitter.com/en) account for your bot
-   Replace your keys in the config(Empty).py file and rename it config.py

        import twitter

        def getApi():
            return twitter.Api(consumer_key='YourKey',
                                consumer_secret='YourKey',
                                access_token_key='YourKey',
                                access_token_secret='YourKey',
                                tweet_mode='extended')
Install all requirements that can be find in requirements.txt file:

You can either use

    $ pip install -r requirements.txt 

Or installing them one by onen but remeber using last versions of these can lead to errors.

    $ pip install python-twitter
    $ pip install requests
    $ pip install discord
    $ pip install rich

### Using it with hand control

    $ ./Executable.py

![CLI picture](https://github.com/PhoqueEberlue/TwitterMarkovBot/blob/master/gitimages/CLIMode.png)

### Setting up the bot

Globaly what I'm doing is just calling scriptbot.bash every hours with my raspberry pi and checking if the user posted since the last refresh. However it's up to you to modify this file to change what you want the bot to do and when.

-   Change the path of RoutineFile.py file in scriptbot.bash

        $ ./scriptbot.bash &

Thanks for reading!

