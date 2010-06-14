import tweetstream

stream = tweetstream.TweetStream("zandermane", "alex18257")

for tweet in stream:
	if tweet.has_key("text"):
		print tweet['user']['screen_name'] + ": " + tweet['text'], "\n"
		print "----" * 4
