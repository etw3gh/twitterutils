import os
import requests
from requests_oauthlib import OAuth1
import sys

unfollowCount = 0
verbose = True

if '-v' in sys.argv or '--verbose' in sys.argv:
  verbose = False

tok = os.environ['YOUR_ACCESS_TOKEN']
ts = os.environ['YOUR_ACCCESS_SECRET']
ck = os.environ['YOUR_CONSUMER_KEY']
cs = os.environ['YOUR_CONSUMER_SEC']

oauth = OAuth1(ck, client_secret=cs, resource_owner_key=tok, resource_owner_secret=ts)

req = requests.get(url="https://api.twitter.com/1.1/friends/ids.json?count=5000", auth=oauth)
following = req.json()['ids']

req = requests.get(url="https://api.twitter.com/1.1/followers/ids.json?count=5000", auth=oauth)
followers = req.json()['ids']


for f in following:
  if f not in followers:
    unfollowCount += 1
    data = { 'user_id': f}
    userData = requests.post(url="https://api.twitter.com/1.1/friendships/destroy.json", auth=oauth, data=data)

    if verbose:
      print('unfollowed: @{}'.format(userData.json()['screen_name']))


print('unfollowed: {} users who did not follow you back'.format(unfollowCount))

