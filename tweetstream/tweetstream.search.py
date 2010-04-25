#!/usr/bin/python
import tweetstream

words = ["tea"]
stream = tweetstream.TrackStream("zandermane", "alex18257", words)

for tweet in stream:
	if tweet.has_key("text"):
		print tweet['user']['screen_name'] + ": " + tweet['text'], "\n"
		print "----" * 4
