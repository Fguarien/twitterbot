#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import csv
import dateutil.parser as dp
from dateutil import tz
import datetime
import pytz

def import_feed(file):
    fn = open(file, 'r')
    f = csv.DictReader(fn)
    feed_list = []

    # iterating over each row and append
    # values to empty list
    for col in f:
        feed_list.append(col['feed_list'])
    return feed_list

class Settings:
    """Twitter bot application settings.

    Enter the RSS feed you want to tweet, or keywords you want to retweet.
    """
    # RSS feed to read and post tweets from.
    feed_urls = import_feed('/Users/hal9000/opt/lab/twitterbot/feed_urls.csv')

    # Log file to save all tweeted RSS links (one URL per line).
    posted_urls_output_file = "posted-urls.log"

    # Log file to save all retweeted tweets (one tweetid per line).
    posted_retweets_output_file = "posted-retweets.log"

    # Include tweets with these words when retweeting.
    retweet_include_words = ["#ai","#ArtificialIntelligence", "#AINews","#CyberSecurity","#ChatGPT"]

    # Do not include tweets with these words when retweeting.
    retweet_exclude_words = []

    # Today date for log file.
    today=datetime.datetime.now(tz.tzlocal())

    aweekago=today-datetime.timedelta(days=7)

class TwitterAuth:
    """Twitter authentication settings.

    Create a Twitter app at https://apps.twitter.com/ and generate
    consumer key, consumer secret etc. and insert them here.
    """
    consumer_key = 
    consumer_secret = 
    bearer_token = 
    access_token = 
    access_token_secret = 


def display_help():
    """Show available commands."""
    print("Syntax: python {} [command]".format(sys.argv[0]))
    print()
    print(" Commands:")
    print("    rss    Read URL and post new items to Twitter")
    print("    rt     Search and retweet keywords")
    print("    help   Show this help screen")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "rss":
            print("tu as mis rss")
        elif sys.argv[1].lower() == "rt":
            print("tu as mis rt")
        else:
            display_help()
    else:
        display_help()
