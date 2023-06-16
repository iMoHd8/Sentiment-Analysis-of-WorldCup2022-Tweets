"# Sentiment-Analysis-of-WorldCup2022-Tweets" 

Using Machine Learning, we developed a system that classifies the hate speech, specifically hate speech of world cup 2022 tweets.
In the development process, we have implemented the dataset on five algorithms (Logistic Regression, Decision Tree, Naive Bayes, SVM, and Random Forest).
The best accuracy was "Logistic Regression", so we built the system using it, and the accuracy is 94% on the dataset has 430k records. also,
we have tried to avoid the "Negation Words" issue by creating a dataset that has many negation words and the alternative of each word,
then the system will check if there is any negation from the dataset, if yes then the word will be replaced by its alternative.

things we used: Logistic Regression Algorithm NLP tools (stopwords, tokenization, n-gram...) Transfer Learning (BERT) Twitter API Django framework

The system can fetch tweets from Twitter and classify each tweet, either from a specific hashtag or Twitter user (public accounts).

and eventually, we developed a website for displaying the results using the Django framework.

Finally, this was a graduation project that we put all our efforts into it. and This is our project in a nutshell.

thanks for your time :)
