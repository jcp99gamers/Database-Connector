# import numpy as np
def Code(word):
    variations = [word.lower(), word.upper(), word.capitalize()]
    for i in range(2 ** len(word)):
        temp = ""
        for j in range(len(word)):
            if (i >> j) % 2 == 1:
                temp += word[j].upper()
            else:
                temp += word[j].lower()
        variations.append(temp)
    return list(set(variations))
def CapitalVariations(word):
    if type(word) == str:
        return Code(word)
    elif type(word) == list:
        temp = []
        for x in word:
            temp.append(Code(x))
        # variations = np.array(temp)
        # return variations
        return temp