# random word match dictionary


import sys
from itertools import permutations
from PyDictionary import PyDictionary





inputstr = 'fcuk'.upper()#input("enter ")#.upper() #sys.argv[1].upper()
k = 4


def word_combination(word_str,lenght):
    if k <= len(inputstr):
        lst_inp = list(inputstr)
    
        perms = (p for p in permutations(lst_inp,k))
        # print(type(perms))

        for p in perms:
            word = ''.join(p)
            print(word)

    else:
        print('u have inserted high number')

word_combination(inputstr,k)



# -----------Dict stuff

# word = "fuck"
# dictionary = PyDictionary(word)
# meaning = dictionary.printMeanings()
# print(f'word is {word} \nmeaning is {meaning}')










