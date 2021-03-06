# -*- coding: utf-8 -*-
"""DataLit-1.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eVfWF-I03KWLJ41Lsa_gdU3aXzr-WOyR
"""

#@title Default title text
# Step 1 - install dependencies
!pip install pandas # Preprocessing
!pip install tweepy # Twitter API library
!pip install twython
!pip install vaderSentiment # Lexicon-based sentiment analysis

# Step 2 - Import Dependencies
import tweepy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

# Step 3 - Configure Twitter API
consumer_key = 'pNJ0JvtCyS9euUasq62IKYK8j'
consumer_secret = 'dAc2nw4gOuvdrQGHKmVUMmjyA2YS7HpAvUJONIwuDcXTbBcGqr'
access_token = '33554253-WbpJzAjZtv2iBkLD4F2v1B7C0dssCKpFRS7DdsV7s'
access_token_secret = 'BOdAoNrvr65aU9b1V29VqlFLsJIe356RvKDoZgRV44G8d'

# Step 4 - Authenticate Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 5 - Define Cleaning Function

import re

def clean_tweet(tweet):
    '''
    Remove links and special characters
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

# Step 6 - Find Related Tweets
tweets = api.search('Donald Trump', count=200)

# Create a clean pandas dataframe as follows
data = pd.DataFrame(data=[clean_tweet(tweet.text) for tweet in tweets], columns=['Tweets'])

display(data.head(10))

print(tweets[0].id)
print(tweets[0].created_at)
print(tweets[0].source)
print(tweets[0].favorite_count)
print(tweets[0].retweet_count)
print(tweets[0].geo)
print(tweets[0].coordinates)
print(tweets[0].entities)

# Gather lexicon data
import nltk
nltk.download('vader_lexicon')

# Step 7 - Go through the tweets to analyze their sentiment

sid = SentimentIntensityAnalyzer()

list = []
for index, row in data.iterrows():
  ss = sid.polarity_scores(row["Tweets"])
  list.append(ss)
se = pd.Series(list)
data['polarity'] = se.values

# We display the first 10 elements of dataframe
display(data.head(100))