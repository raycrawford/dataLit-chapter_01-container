#!/usr/bin/python3

# Load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()

# Split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
tokens = [w.lower() for w in tokens]

# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# Remove remaining tokens that are not alphabetic
words = [word.lower() for word in tokens if word.isalpha()]

# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

# stemming of words
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]

print(stemmed[:100])

