#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy

def send_msg(msg):
#enter the corresponding information from your Twitter application:
    CONSUMER_KEY = 'nAb94wMnaytHdnZWmnNFoPjZv'#keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = '9eBy2OVMRmqAhVAmhBvdZrI1swAPYvUS70PChTKwQWbzO5WtEM'#keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = '860849886299914241-dtth1rjkN2OB8jU6UwMQGLJdAlXRO8U'#keep the quotes, replace this with your access token
    ACCESS_SECRET = 'RR8IlNsXNWtJ8kceNrln1MiaMW6ae9s2gErHjS1k7p5s8'#keep the quotes, replace this with your access token secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(status=msg)
