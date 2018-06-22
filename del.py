from twitter import *
import os
import sys

rtCount = 0
twCount = 0

delTweets = True
delRetweets = True
verbose = False

if '-v' in sys.argv or '--verbose' in sys.argv:
  verbose = True

if '--del-rts' in sys.argv:
  delRetweets = True


if '--just-rts' in sys.argv:
  delTweets = False
  delRetweets = True

tok = os.environ['YOUR_ACCESS_TOKEN']
ts = os.environ['YOUR_ACCCESS_SECRET']
ck = os.environ['YOUR_CONSUMER_KEY']
cs = os.environ['YOUR_CONSUMER_SEC']
screen_name = os.environ['yourtwitterhandle']

t = Twitter(auth=OAuth(tok, ts, ck, cs))
tweets = t.statuses.user_timeline(
  screen_name=screen_name,
  count=200
)

if verbose:
  print('found {} statuses'.format(len(tweets)))

for tweet in tweets:
  if 'retweeted_status' in tweet and delRetweets:
    r = t.statuses.unretweet(id=tweet['id'])
    rtCount += 1
  else:
    if delTweets:
      r = t.statuses.destroy(id=tweet['id'])
      twCount += 1

if verbose and delTweets: 
  print('{} tweets deleted'.format(twCount))

if verbose and delRetweets:
    print('{} rts deleted'.format(rtCount))
