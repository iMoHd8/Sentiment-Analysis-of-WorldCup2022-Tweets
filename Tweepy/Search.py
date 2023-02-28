import tweepy
from . import Config
    
def get_tweets_from_user(user_name):
    client = tweepy.Client(bearer_token=(Config.Bearer_Token))
    
    tweets = []
    
    if user_name.startswith('@'):
        user_name = user_name.replace('@', '')
        user = client.get_user(username=(user_name))
        user_id = user.data.id
    else:
        user = client.get_user(username=(user_name))
        user_id = user.data.id

    users = client.get_users_tweets(id=user_id, exclude=['replies','retweets'], tweet_fields=['lang'] , max_results= 100)
    
    for user in users.data:
        if user.lang == 'en':
            tweets.append(user.text)
        
        
    if len(tweets) == 0:
        return 'Sorry, there are no English language tweets from this user'
        
    else:
        return tweets
    




def get_tweets_using_hashtag(hashtag):
    client = tweepy.Client(bearer_token=(Config.Bearer_Token))
    
    tweets = []

    
    respons = client.search_recent_tweets(query= (hashtag + ' -is:retweet'), max_results= 100, tweet_fields=['lang'])
    
    for tweet in respons.data:
        if tweet.lang == 'en':
            tweets.append(tweet.text)
        else:
            pass
    
    if len(tweets) == 0:
        text = ['Sorry, there are no English language tweets from this user']
        return text
        
    else:
        return tweets

    
    

