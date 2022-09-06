f = open("lyrics.txt", 'r')
content = f.read()
words = content.split()
#method 1:use for loop
for word in words:
    print('{0}: {1}'.format(word, words.count(word)))
#method 2:use collections
import collections
print(collections.Counter(words))