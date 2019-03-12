#!/usr/bin/python3

filename = './2600-0.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

words = text.split()
print(words[:100])
