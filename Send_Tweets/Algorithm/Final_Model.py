import pandas as pd
import re, nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
from textblob import TextBlob
from .CleaningTheDataset import process_tweet



NS = pd.read_csv('Send_Tweets\\Algorithm\\Negation Handling\\negation.csv', encoding='unicode_escape')
negation_dict = NS.set_index('negation')['alternative'].to_dict()

def NegationHandling(text):    
    # Replace the negation sentences with their alternatives
    for negation, alternative in negation_dict.items():
        for i in range(len(text)):
          text = text.replace(negation, alternative)
    
    return text



def Data_Processing(text):
    text = process_tweet(text)

    return text



def stemming(data):
    stemmer = PorterStemmer()
    text = [stemmer.stem(word) for word in data]
    return data



def load_model():
    vectors_file = open("Send_Tweets\\Algorithm\\vectors.sav", 'rb')
    vectors = pickle.load(vectors_file)
    vectors_file.close()
    model_file = open('Send_Tweets\Algorithm\sentiment_model.sav', 'rb')
    model = pickle.load(model_file)
    model_file.close()
    
    return vectors, model



def predict(vectors, model, text):
    text = NegationHandling(text)
    text = Data_Processing(text)
    vectors_text = vectors.transform(stemming(text))
    sentiment = model.predict(vectors_text)
    sentiment_pred = model.predict_proba(vectors_text)
    
    print(text)
    return sentiment, sentiment_pred



def sentiment_Analize(text):
    vectors, model = load_model()
    
    sentiment = predict(vectors, model, text)
    print(sentiment[1][0])

    return sentiment[0], sentiment[1]



