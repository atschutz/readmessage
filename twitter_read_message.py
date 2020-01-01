import os
import random
import tweepy

import make_message

auth = tweepy.OAuthHandler(os.environ['READ_MESSAGE_API_KEY'], 
                           os.environ['READ_MESSAGE_API_SECRET_KEY'])

auth.set_access_token(os.environ['READ_MESSAGE_ACCESS_TOKEN'],
                      os.environ['READ_MESSAGE_ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)

if (random.randint(1,8) == 1): #TODO set to 1 in 8 for scheduled tweeting.
    api.update_status(make_message.makeCapitalizedMessage())

