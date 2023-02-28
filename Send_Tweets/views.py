from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from .Algorithm.Final_Model import *

# Create your views here.

def Sentiment_Analyzer(request):
    if request.method == 'POST':
        message = request.POST['tweet_text']
        print(request.POST) 
        
        sentiment = sentiment_Analize(message)
        print(float(sentiment[1][0][2]) * 100)
        print(float(sentiment[1][0][1]) * 100)
        print(float(sentiment[1][0][0]) * 100)
        text = message
        text = NegationHandling(message)
        #text = Data_Processing(message)
        text = "".join(text)

        context = {'sentiment': sentiment[0][0], 'content': text, 'positive_per': format(float(sentiment[1][0][2])* 100, '.2f'), 'negative_per' : format(float(sentiment[1][0][0])* 100, '.2f'), 'neutral_per': format(float(sentiment[1][0][1]) * 100, '.2f')}

        return render(request, 'Tweet_Sentiment.html', context)

    return render(request, 'Tweet_Sentiment.html')


def Home(request):

    return render(request, 'Home.html')