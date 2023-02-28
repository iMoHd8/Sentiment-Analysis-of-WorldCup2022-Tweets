from django.shortcuts import render
from django.http import *
from Tweepy.Search import *
from Send_Tweets.Algorithm.Final_Model import *
# Create your views here.


def Fetch_Tweets(request):
    if request.method == 'POST':
        message = request.POST['ID']
        print(message)

        if message.startswith('@'):
            Fetching_Tweets = get_tweets_from_user(message)
            Tweets = []
            tweets_and_sentiment_list = []

            for i in Fetching_Tweets:
                sentiment = sentiment_Analize(i)
                text = i
                text = NegationHandling(text)
                #text = Data_Processing(text)
                text.capitalize
                text = "".join(text)
                Tweets.append(text)
                tweets_and_sentiment_list.append((i,sentiment[0][0].capitalize))

            context = {'tweets': tweets_and_sentiment_list}
            return render(request, 'Fetch_Tweets.html', context)

            
        elif message.startswith('#'):
            Fetching_Tweets = get_tweets_using_hashtag(message)
            Tweets = []
            tweets_and_sentiment_list = []

            for i in Fetching_Tweets:
                sentiment = sentiment_Analize(i)
                text = i
                text = NegationHandling(text)
                #text = Data_Processing(text)
                text = "".join(text)
                Tweets.append(text)
                tweets_and_sentiment_list.append((i,sentiment[0][0]))
                
            context = {'tweets': tweets_and_sentiment_list}
            return render(request, 'Fetch_Tweets.html', context)
        
        else:
            return HttpResponseBadRequest("Please Enter a Valid Values")
        

    return render(request, 'Fetch_Tweets.html')