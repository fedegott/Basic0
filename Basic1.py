
#iterate through characters of a collections of string

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
print(a+'f')