import tweepy
import csv
import pandas as pd
import ast

#Getting Creds from TOKENS
PersonalCredsRaw = open('TOKENS', 'r')
PersonalCreds = ast.literal_eval(PersonalCredsRaw.read())

consumer_key = PersonalCreds["consumer_key"]
consumer_secret = PersonalCreds["consumer_secret"]
access_token = PersonalCreds["access_token"]
access_token_secret = PersonalCreds["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
counter = 1
#csvFile = open('tweetersnotime.csv', 'a')
#Use csv Writer
#csvWriter = csv.writer(csvFile)
tweetcounter = 1
tweetdict = {}

tweetList = []
tweetListime = []

for tweet in tweepy.Cursor(api.search,q="#india",count=100,lang="en",since="2017-04-03").items():
    #print (tweet.created_at, tweet.text)
    tweetDict = { 
                'Timestamp' : tweet.created_at,
                'Tweet' : tweet.text
    }
    #tweetdict = { tweet.created_at : tweet.text.encode('utf-8')}

    tweetListime.append(tweetDict['Timestamp'])  
    tweetList.append(tweetDict)
    counter+=1

    if counter==500:
        break

    
#16453 tweets in total
for i in tweetList :
    print (i)
    print ("\n")

    tweetcounter+=1

for j in tweetListime :
    print (i)
    print ("\n")
    


print ("Total tweets : ",tweetcounter)

#csvFile.close()