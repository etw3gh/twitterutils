# Twitter Account Utils

## about

Very basic utils to manage your personal twitter account without resorting to third party apps

### requirements

  del.py uses the twitter library

  unfollow.py and unfav.py use the twitter REST api

  see requirements.txt

### config

  Create a [twitter app](https://apps.twitter.com/) and generate your tokens

  Save as environment variables:

    tok = os.environ['YOUR_ACCESS_TOKEN']
    ts = os.environ['YOUR_ACCCESS_SECRET']
    ck = os.environ['YOUR_CONSUMER_KEY']
    cs = os.environ['YOUR_CONSUMER_SEC']
    screen_name = os.environ['yourtwitterhandle']

  Or just hardcode them:

    tok = 'YOUR_ACCESS_TOKEN'
    ts = 'YOUR_ACCCESS_SECRET'
    ck = 'YOUR_CONSUMER_KEY'
    cs = 'YOUR_CONSUMER_SEC'
    screen_name = 'yourtwitterhandle'

### console output

append to param list

    -v

    --verbose


### limits

Run the scripts however many times it take to clear your account

## Unfollow non followers

  python unfollow.py -v

## Delete Tweets and Retweets

Delete tweet statuses only:

    python del.py -v

Delete tweets and retweets: 

    python del.py --del-rts -v

Delete retweets only:

    python del.py --just-rts -v


## Delete Likes

  python unfav.py