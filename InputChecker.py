import numpy as np
def Code(word):
    ChildList = []
    lowercase_word = word.lower()
    for i in range(2**len(lowercase_word)):
        binary = format(i, '0' + str(len(word)) + 'b')
        new_word = ""
        for j in range(len(word)):
            if binary[j] == "1":
                new_word += word[j].upper()
            else:
                new_word += word[j].lower()
        # print(new_word)
        ChildList.append(new_word)
    return ChildList

def CapitalVariations(word):
    ParentList = []
    if type(word) == str:
        ParentList = Code(word)
    elif type(word) == list:
        for Child in word:
            ParentList += Code(Child)
    return ParentList