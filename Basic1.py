
#iterate through characters of a collections of string
# below is a NESTED for loop
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

word = 'jose'
a = []
for w in word:
    a.append(w)
print(a)


#List comprehension --> need to be flanked by [ ]

a = [x*x for x in range(5)]

c = "".join(wordlist)
d = [ word[i] for word in wordlist for i in range(len(word))]

