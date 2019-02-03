import sys
from ast import literal_eval

try:
    import praw
except Exception as e:
    print ("ERROR Importing PRAW+\n", e)
    sys.exit()

#Create Reddit instance
print ("Reddit: Token Reading")
try:
    RedditTokenData_raw = open('RedditTokens','r')
    RedditTokenData = literal_eval(RedditTokenData_raw.read())
    client_id = RedditTokenData['client_id']
    client_secret = RedditTokenData['client_secret']
    user_agent = RedditTokenData['user_agent']

except Exception as e:
    print ("\tERROR\n\t", e)
    sys.exit()

#Create Reddit instance
print ("Reddit: Instance Creation")
try:
    reddit = praw.Reddit(
                        client_id = client_id,
                        client_secret = client_secret,
                        user_agent = user_agent
                        )

except Exception as e:
    print ("\tERROR\n\t", e)
    sys.exit()
