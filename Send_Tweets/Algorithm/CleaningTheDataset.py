import pandas as pd
import re
import pickle

# for datasets:
# Tweets = pd.read_csv('Name of The Dataset', encoding="utf8")

# for normal text
# Tweets = ['']

def process_tweet(tweet):
    
    tweet = [tweet]
    
    # Naming x as the name of first column which will be the tweets text and for not changing it everytime and with every new dataset.
    # x = tweet.columns[0]

    for sentence in range(0, len(tweet)): 
        processed_feature = re.sub('', '', str(tweet[sentence]))
        processed_feature = re.sub('https?\S+', '', processed_feature, flags=re.MULTILINE) #Remove links
        processed_feature = re.sub(r"#\S*", ' ', processed_feature) #Remove Hashtags
        processed_feature = re.sub(r"@\S*\s", ' ', processed_feature) #Remove Mentions
        processed_feature = re.sub(r"[?]*\s", ' ', processed_feature) #Remove a ? sign
        processed_feature = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_feature) #Remove a Single Character 
        processed_feature = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_feature) #Remove a Single Character if it The First Character in The Line
        processed_feature = re.sub(r'\s+', ' ', processed_feature) #Remove More One Space
        processed_feature = re.sub(r"\W", ' ', processed_feature) #Keep Only Words
        processed_feature = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_feature) #Remove a Single Character if it The First Character in The Line
        processed_feature = re.sub(r'  +', ' ', processed_feature)
        processed_feature = processed_feature.lower() #Make All Character in Lower Case
      
        tweet[sentence] = processed_feature #Changing The Original Sentence to Cleaned Sentence
        
    # print(tweet)
    return tweet

#Save The Changes in New File
# Tweets.to_csv('Cleaned Dataset.csv') 