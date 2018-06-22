import os
import requests
from requests_oauthlib import OAuth1

tok = os.environ['YOUR_ACCESS_TOKEN']
ts = os.environ['YOUR_ACCCESS_SECRET']
ck = os.environ['YOUR_CONSUMER_KEY']
cs = os.environ['YOUR_CONSUMER_SEC']

oauth = OAuth1(ck, client_secret=cs, resource_owner_key=tok, resource_owner_secret=ts)

req = requests.get(url="https://api.twitter.com/1.1/favorites/list.json?count=200", auth=oauth)
count = 0

for fav in req.json():
  id = fav['id']
  data = {'id' : id}
  response = requests.post(url="https://api.twitter.com/1.1/favorites/destroy.json",auth=oauth,data=data)
  count += 1

print('{} favs deleted'.format(count))
