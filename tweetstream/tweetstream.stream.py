import tweetstream

global_stream = tweetstream.TweetStream("zandermane", "alex18257")

for tweet in global_stream:
	if tweet.has_key("text"):
		print "----" * 4 + "->"
		print tweet['user']['screen_name']
		print tweet['user']['location']
		print tweet['text']
		print "----" * 4 + "\n"
