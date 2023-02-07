import re

def afunction():
    print("This is the installed function")

def clean_string(str_word):
    """
    INPUTS:
    str_word     string string contining several words to clean
    RETURNS:
    string       the string after removal of extra spaces, punctuation and lowercasing
    """
    str_word = re.sub(r'\W+', ' ', str_word)
    assert isinstance(str_word, str), "String expected but recieved type {} instead".format(type(str_word))

    return str_word.strip()

import re
def space_compress(stocomp):
    assert isinstance(stocomp, str), "Expected str but got {} instead".format(type(stocomp))
    comp = re.sub(r'\s+', ' ', stocomp)
    return comp.strip()

def new_func():
    pass

def Obnoxious_Edit(str_word):
    res = ""
    for i in range(len(str_word)):
        if str_word[i].upper() == "I":
            res = res + str_word[i].lower()
        elif str_word[i].upper() == "L":
            res = res + str_word[i].upper()
        elif str_word[i].upper() == "E":
            res = res + "333"
        elif str_word[i].upper() == "O":
            res = res + "0"
        elif str_word[i].upper() == "A":
            res = res + "@"
        elif str_word[i].upper() == "Y":
            res = res + "ii"
        elif i % 2: 
            res = res + str_word[i].lower()
        else:
            res = res + str_word[i].upper()
    return res

def PigLatinify(str_word):
    sentence = str_word.split()
    new = ""
    for word in sentence:
        if word[0].upper() in ['A','E', 'I', 'O', 'U']:
            P =  word.lower() + "way"
        elif word[0:2].upper() in ['SH', 'ST', 'SM',  'GL', 'TH', 'FL', 'QU']:
            P = word[2:] + word[0:2].lower() + "ay"
        else:
            P = word[1:] + word[0].lower() + "ay"
        new = new + str(P) + " "

    return new


 

