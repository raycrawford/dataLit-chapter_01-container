#!/usr/bin/python3

filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# Split into words by white space
words = text.split()
print(words[:100])

# Remove punctuation from each word
import string
words = [word.lower() for word in words]
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print (stripped[:100])
