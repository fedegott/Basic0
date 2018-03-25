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
a=4
import numpy as np
string = 'a b c d e f g h i j k l m n o p q r s t u v w x y z ' #determines the possibilities
result = 'methinksitislikeaweasel' #can't use spaces unless they're also added to the string

def randomword(string):
    ars = string.split()
    rand = np.random.randint(0,len(ars))
    return ars[rand]

# final ='1'
# while final != result:
#     alist = []
#     for i in range(len(result)):
#         alist.append(randomword(string))
#
#     final = "".join(alist)
#     print(final)

alist = []
lista = []
final = '1'
for i in range(len(result)):
    while final != result[i]:
        # alist.append(randomword(string))
        # final = "".join(alist)
        final = randomword(string)
        print(final)
        if(final == result[i]): lista.append(final)
        # else: alist.pop()
        print(lista)
