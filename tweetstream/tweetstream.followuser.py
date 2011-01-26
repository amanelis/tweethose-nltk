#!/usr/bin/python
import tweetstream

users = [1, 454]
stream = tweetstream.FollowStream("username", "password", users)

for tweet in stream:
	print "Got tweet from: ", tweet["user"]["screen_name"]
