import json

# create a dictionary to store your twitter credentials

twitter_cred = dict()

# Enter your own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = 'mJ2fluR2xOZaj5byk68urYhRl'
twitter_cred['CONSUMER_SECRET'] = 'c0lmSii3lq436Oh9Lyp2vsIkxj2fLMTVaCfVbi8xoX1L6kXJJ2'
twitter_cred['ACCESS_KEY'] = '1048889324052275200-hVDEZ5I7L7wQLx2KclPnACpj982rcx'
twitter_cred['ACCESS_SECRET'] = 'eI7pR91fjbVSrGNVGRUbd6CEVEIp82rkUMmiPhH9xlK5j'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public

with open('twitter_credentials.json', 'w') as secret_info:
	json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)