import json
import random

class MarkovChain:
    def __init__(self, filename):
        self._filename = filename #The json's name
        self._data = None #The json file stored into a python variable
        self._probDict = {}
        self._startingWords = []
        self._endingWords = []
        self._coef = 0.5 #The higher, the longer tweets. The lower, the shorter tweets
    
    def setData(self):
        with open(self._filename, "r", encoding="utf-8") as read_file:
            self._data = json.load(read_file)
    
    def getData(self):
        return self._data
    
    def setProbDict(self):
        self.setData()
        dataList = []
        for tweet in self._data.keys():
            tweetWordList = self._data[tweet]["text"].split()
            self._startingWords.append(tweetWordList[0])
            self._endingWords.append(tweetWordList[-1])
            for word in tweetWordList:
                dataList.append(word)
        for i in range(len(dataList)-1):
            currentWord = dataList[i]
            nextWord = dataList [i+1]
            if currentWord in self._probDict.keys():
                if nextWord in self._probDict[currentWord].keys():
                    self._probDict[currentWord][nextWord] += 1
                else:
                    self._probDict[currentWord][nextWord] = 1
            else:
                self._probDict[currentWord] = {nextWord: 1}
                
    def getProbDict(self):
        return self._probDict
    
    def generateTweet(self):
        self.setProbDict()
        word = random.choice(self._startingWords)
        res = word
        i = 0
        condition = True
        while condition:
            parantheseCheck = False
            i += 1
            nextWordList = []
            try:
                for (nextWord, num) in self._probDict[word].items():
                    nextWordList.extend([nextWord]*num)
            except KeyError:
                break
            word = random.choice(nextWordList)
            res += ' ' + word
            if random.random() > 0.5:
                if word in self._endingWords:
                    condition = False
        openP = 0
        closeP = 0
        for char in res:
            if char == "(":
                openP += 1
            if char == ")":
                closeP += 1
        if openP > closeP:
            res += ")"*(openP-closeP)
        return res
    
    def setCoef(self, coef):
        self._coef = coef
        
    def getCoef(self):
        return self._coef