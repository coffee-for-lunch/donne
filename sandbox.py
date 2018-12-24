import tweepy
import openpyxl
import os
import time

# api gobldeegook

api_key = 'j0DjoY9PiefL03iFZitUMNKu9'
api_secret_key = 'rkVO9vI5obsFYEL6VDc0XM0sL5aveB2HDTufIs3CB6PSVqgslQ'
access_token = '4843888401-N8HbBgDLjV07Z3lF46XLWpvK1uZVcJajySZsWTf'
access_token_secret = 'bs3kHfPPx9EVXOnamCNqPqlhFhK4D92TY2m8L2o3MbGjR'

auth = tweepy.OAuthHandler(api_key, api_secret_key)

auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# grabbing the poems

workbook = openpyxl.load_workbook(os.getcwd() + '/Donne.xlsx', data_only=True)
sheet = workbook['Songs and Sonets']
line = sheet['B6'].value
line2 = sheet['B7'].value


# now tweet!

api.update_status(status = line)
time.sleep(120)
api.update_status(status = line2)
