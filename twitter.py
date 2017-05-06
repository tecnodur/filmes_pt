#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy
from secrets import CONSUMER_KEY
from secrets import CONSUMER_SECRET
from secrets import ACCESS_KEY
from secrets import ACCESS_SECRET



def send_msg(msg):
#enter the corresponding information from your Twitter application:

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(status=msg)
