import tweepy
import csv
from tweepy import Stream
from tweepy import OAuthHandler

consumer_key = 'QWRrxAhLDVQqSXsvtl2n1sV9b'
consumer_secret = 'bhMxKL6gUlNTYHmze70oij09trtl7eM8QWxlwoIOeY2RRYjt6J'
access_token = '134878415-fiYoDxK1IGLKSlf0Q7XvcHtnnACuVcmVZRGUxlF6'
access_secret = 'vvPzBJ6PYKEdkormziBosOuzYErI2CzbNqM3Djkxs81qF'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#csvFile = open('tweet_result.csv', 'a')
#csvWriter = csv.writer(csvFile) 
api = tweepy.API(auth,wait_on_rate_limit=True)

#results = api.search(q = "nba", lang = "en", count=2000, tweet_mode = 'extended')
query = 'nba'
max_tweets = 100
#results = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

results = []
last_id = -1
while len(results) < max_tweets:
    count = max_tweets - len(results)
    try:
        new_tweets = api.search(q=query, count=count, tweet_mode = 'extended', max_id=str(last_id - 1))
        if not new_tweets:
            break
        results.extend(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
        break

c=1
n=10

tweet_chunks = [results[i * n:(i+1) * n] for i in range((len(results) + n - 1) // n)]

#print("Result:", results)
#print("\nChunks:", tweet_chunks)
#print(results)
#print(len(results))
#print(len(tweet_chunks))
#print(len(tweet_chunks[0]))
for result in tweet_chunks:
	with open('tweetOneDay'+str(c)+'.txt', 'w') as output:
		for result2 in result:
			output.write("%s" % result2.full_text)
	output.close()
	c += 1
'''
for result in results:
  print(result.full_text)
'''
