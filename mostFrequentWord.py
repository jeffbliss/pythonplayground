#!/usr/bin/python3

print("Enter a whitespace separated sentence and I'll tell you which word occured the most")

response = input()
wordList = response.split(' ')
mostFrequentWord = wordList[0]

for item in wordList:
    itemCount = wordList.count(item)
    if itemCount > wordList.count(mostFrequentWord):
        mostFrequentWord = item

print("your most frequently used word first encountered was (not counting ties):", mostFrequentWord)