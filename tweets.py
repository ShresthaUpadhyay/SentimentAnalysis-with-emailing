import GetOldTweets3 as got



def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees')\
                                           .setSince("2015-05-01")\
                                           .setUntil("2015-09-30")\
                                           .setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    print(tweet.text)

def get_tweets_byUsername():
    tweetCriteria = got.manager.TweetCriteria().setUsername("narendramodi")\
                                           .setTopTweets(True)\
                                           .setMaxTweets(10)
    # list of stored in tweets in the form of objects in tweets variable                                        
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    tweet_text = [[tweet.text]for tweet in tweets] 
    return tweet_text


# get_tweets() 
 

text = ""
list_tweets = get_tweets_byUsername() 

# print('Enter the name of file you want to store the tweets:')
file_name = input('Enter the name of file you want to store the tweets:')

for i in range(0,len(list_tweets)):
    with open(file_name+'.txt', '+a') as output:
        # text = list_tweets[i][0] + ' ' + text
        output.write(list_tweets[i][0])

print(type(text))
# print(list_tweets)


