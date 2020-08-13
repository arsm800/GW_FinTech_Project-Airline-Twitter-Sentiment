#!/usr/bin/env python3

import pandas as pd
import os
import dotenv
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from tweepy import Stream 
from tweepy.streaming import StreamListener
import time
import datetime



def login_to_twitter():

    dotenv.load_dotenv()

    consumer_key = os.getenv("twitter_api_key")
    consumer_secret = os.getenv("twitter_api_secret_key")
    access_token = os.getenv("twitter_access_token")
    access_token_secret = os.getenv("twitter_access_token_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True)

    return api


def scrape_tweets(api, text_query, count):

    tweets = []

    try:
    # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count, lang='en'):

            # Adding to list that contains all tweets
            tweets.append((tweet.created_at, tweet.user.location, tweet.coordinates, tweet.id, tweet.text))

        # Creation of dataframe from tweets list
        tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Place', 'Place_coord_boundaries', 'Tweet Id', 'Text'])

        # Converting dataframe to CSV
        tweetsdf.to_csv('{}-tweets_{}.csv'.format(text_query, datetime.datetime.now())) 

    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)



    

# api = login_to_twitter()

# test = scrape_tweets(api, ['Mexico', 'United Airlines'])

# print(test)



count = 18000


def iterate_scrape():

    print(time.ctime())

    text_query = "United Airlines"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "UAL"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "Delta Airlines"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "DAL"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "Southwest Airlines"
    scrape_tweets(login_to_twitter(), text_query, count)
    
    text_query = "LUV"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "American Airlines"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "AAL"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "JetBlue"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "JBLU"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "Alaska Airlines"
    scrape_tweets(login_to_twitter(), text_query, count)

    text_query = "ALK"
    scrape_tweets(login_to_twitter(), text_query, count)


while True:

    iterate_scrape()

    time.sleep(7200)



