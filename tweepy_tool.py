import tweepy
import sys
from matplotlib import pyplot as plt
from datetime import datetime

# credentials stored in different file
import twitter_credentials

# variables
tweets_per_hour = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# method to create the graph
def create_graph(username):
	x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
	y = tweets_per_hour

	plt.bar(x, y, label='Bars1')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Hot time using twitter for ' + username)
	plt.legend()
	plt.show()

# group tweet hour into an array to create an array
def sort_tweet(tweetToAnalyse):
	tweets_per_hour[tweetToAnalyse.hour-1] += 1

# method to analyse each tweet and increment the array with the hour in which it occured
def analyse_tweets(username):
	auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
	auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	count = 0
	for tweet in tweepy.Cursor(api.user_timeline, id=username).items(3000):
		count += 1

		timestamp = tweet.created_at.strftime("%d-%b-%Y (%H:%M:%S.%f)")
		print(str(count) + ' ' + timestamp)
		sort_tweet(tweet.created_at)

# main
if __name__ == '__main__':
	# receive parameters from stdin
	if len(sys.argv) == 2:
		analyse_tweets(sys.argv[1])
		print(tweets_per_hour)
		print('creating graph for ' + sys.argv[1])
		create_graph(sys.argv[1])
	else:
		print "Please insert a username to analyse"