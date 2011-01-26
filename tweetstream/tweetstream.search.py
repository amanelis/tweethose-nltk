#!/usr/bin/python
import tweetstream
import time

words = ["tea"]
stream = tweetstream.TrackStream("zandermane", "alex18257", words)

time.sleep(1)
print "Waiting for tweets.."

for tweet in stream:
	if tweet.has_key("text"):
		print tweet['user']['screen_name'] + ": " + tweet['text'], "\n"
		print "----" * 4
