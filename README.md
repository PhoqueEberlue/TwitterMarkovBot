# TwitterMarkovBot
This is a twitter bot that collects data from an user, in order to tweet based on the Markov Chain principle.

## How to use it ?

Pre Requirements: Python 3, Python twitter, an Twitter developper account

First, put your API keys that you can find at https://developer.twitter.com/en/apps/ and copy paste the different keys in the area made for it in the config.py file.

Then you have to get the ID of the account that you want to gather tweets https://tweeterid.com/
and put it in the bot.py file at the line 39.

Finaly just launch bot.py script by using a cmd or the .bat file.

![Screenshot](img/CommandExample.png)

## How does it work ?

First you should probably do some research on Markov chain, because it can be used in many different situation, and this project here is just one of the uses of it.

The example that i've picked below is really simple as i want to explain the principle of the Markov Chain, but you can use as much data as you want (as soon as your pc has enough performances to run the program). I've put a part of an huge dictionnary at the end.

![Screenshot](img/SimpleExplanation.png)

### The input

## Gathering data



## Using the Markov Chain principle

As you can see, a dictionnary is created based on the data that is gathered by the twitter API:
    The keys of this dictionnary are each words used in the data
    The values of these keys are an other dictionnary which contains:
        as key, the word that follows the word in the base dictionnary
        as value, the number of time that this word follows the word in the base dictionnary.

The starting words list contains the words that are after an ending ponctuation like ".", "!", "?", "...".

The ending words list contains the words that are before an ending ponctuation like ".", "!", "?", "...".

### The output

The algorithm works like this:
-   Take an random word from the starting words
-   while word isn't an ending word:
    -   add a random word that follows the previous word to the sentence (but with probabilities ex: 'it': {'is': 2, 'looks': 1} → you have more chances to pick 'is' than to pick 'looks')
-   return the sentence

## Can i help you ?

Sure ! Don't hesitate to propose some upgrades by doing commits, i will make sure to tell you what i'm thinking about those changes.

## That's a lot of data !

![Screenshot](ALotOfData.png)