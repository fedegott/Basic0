#
# #iterate through characters of a collections of string
# # below is a NESTED for loop
# wordlist = ['cat','dog','rabbit']
# letterlist = [ ]
# for aword in wordlist:
#     for aletter in aword:
#         letterlist.append(aletter)
# print(letterlist)
#
# word = 'jose'
# a = []
# for w in word:
#     a.append(w)
# print(a)
#
#
# #List comprehension --> need to be flanked by [ ]
#
# a = [x*x for x in range(5)]
#
# c = "".join(wordlist)
# d = [ word[i] for word in wordlist for i in range(len(word))]

import numpy as np

alist = []
string = 'a b c d e f g h i j k l m n o p q r s t u v w x y z '
result =  'ho'#'methinks it is like a weasel'

def randomword(string):
    ars = string.split()
    rand = np.random.randint(0,25)
    return ars[rand]

while alist != result:
    for i in range(26):
       alist.append(randomword(string))

print(alist)
