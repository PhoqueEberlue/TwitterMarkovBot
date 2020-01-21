# coding: utf-8
from random import randint


def Extraction_From_TXT(Data_File):
    """
    parameters: a txt file (str)
    result: a list of every words used in the txt
    """
    data = open(Data_File, "r",
                encoding="utf-8")
    Word_List = []
    for word in data.read().split():  # .split() splits each items if they are separated by " " or "\n"
        Word_List.append(word)
    data.close()
    return Word_List


def Probability_Per_Word(Data_File):
    """
    parameters: a txt file (str)
    result: a dictionnary of probabilities
    """
    Word_List = Extraction_From_TXT(Data_File)
    Word_assembly = set(Word_List)
    Word_assembly_list = []
    Word_dictionnary = {}
    for word in Word_assembly:
        Word_assembly_list.append(word)
    for i in range(len(Word_List) - 1):
        if Word_List[i] in Word_dictionnary.keys():
            if Word_List[i+1] in Word_dictionnary[Word_List[i]].keys():
                Word_dictionnary[Word_List[i]][Word_List[i+1]] += 1
            else:
                Word_dictionnary[Word_List[i]][Word_List[i+1]] = 1
        else:
            Word_dictionnary[Word_List[i]] = {}
            Word_dictionnary[Word_List[i]][Word_List[i+1]] = 1
    return Word_dictionnary

#print(Probability_Per_Word('Data.txt')) #if you want to see the dictionnary that is generated

def Starting_And_Ending_Words(Data_File):
    """
    parameters: a txt file (str)
    result: a tuple with the list of the starting words and the list of the endings words 
    """
    Word_List = Extraction_From_TXT(Data_File)
    Starting_Words = []
    Starting_Words.append(Word_List[0])
    Ending_Words = []
    Ending_Words.append(Word_List[-1])
    for i in range(len(Word_List)):
        if Word_List[i][-1] == '.' or Word_List[i][-1] == '!' or Word_List[i][-1] == '?' or Word_List[i][-1] == '¶':
            Ending_Words.append(Word_List[i])
            if i < len(Word_List) - 1:
                Starting_Words.append(Word_List[i+1])
    return {'StartingWords': Starting_Words, 'EndingWords': Ending_Words}


def Generating(Data_File):
    """
    parameters: a txt file (str)
    result: a sentence generated with the markov chain principle
    """
    Word_dictionnary = Probability_Per_Word(Data_File)
    Starting_Words = Starting_And_Ending_Words(Data_File)['StartingWords']
    Ending_Words = Starting_And_Ending_Words(Data_File)['EndingWords']
    First_random = randint(0, len(Starting_Words) - 1)
    res = Starting_Words[First_random]
    Word = Starting_Words[First_random]
    while Word not in Ending_Words:
        Ocurrences = []
        for (WordO, number) in Word_dictionnary[Word].items():
            Ocurrences.extend([WordO]*number)
        Word = Ocurrences[randint(0, len(Ocurrences) - 1)]
        res += ' ' + Word
    return res


def Output(Data_File, n):
    """
    parameters: the data file (str), the output file (str), the number of sentence you want (int)
    result: None, this function modify the output file
    """
    res = ''
    for _ in range(n):
        res += Generating(Data_File) + '\n'
    return res
