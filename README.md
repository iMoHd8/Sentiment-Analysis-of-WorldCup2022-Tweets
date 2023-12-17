# Sentiment Analysis of WorldCup2022 Tweets

## Overview

Welcome to the Sentiment Analysis of WorldCup2022 Tweets project! This system utilizes machine learning to classify hate speech in tweets related to the World Cup 2022. We have implemented and compared five algorithms (Logistic Regression, Decision Tree, Naive Bayes, SVM, and Random Forest) using a dataset containing 430,000 records. After rigorous testing, the "Logistic Regression" algorithm demonstrated the best accuracy at 94%, and thus, it became the foundation of our system.

## Negation Words Handling

To address the challenge of negation words, we created a specialized dataset containing various negation words and their alternatives. During classification, the system checks for the presence of negation words in tweets and substitutes them with their alternatives, ensuring a more accurate sentiment analysis.

## Technologies Used

- **Logistic Regression Algorithm:** Chosen for its superior performance in accuracy.
- **NLP Tools:** Leveraged tools such as stopwords, tokenization, and n-grams to enhance natural language processing.
- **Transfer Learning (BERT):** Employed for advanced language understanding and sentiment analysis.
- **Twitter API:** Used to fetch tweets dynamically from Twitter, allowing classification based on specific hashtags or Twitter users (public accounts).
- **Django Framework:** Developed a web application to showcase and visualize the sentiment analysis results.

## System Capabilities

The system has the following key features:

- **Tweet Classification:** Automatically classifies tweets into categories, distinguishing hate speech from non-hate speech.
- **Dynamic Tweet Fetching:** Utilizes the Twitter API to fetch and analyze tweets based on specific hashtags or Twitter users.
- **Negation Word Handling:** Mitigates the impact of negation words on sentiment analysis through a specialized dataset.
- **Web Interface:** A user-friendly website built using the Django framework to display and interact with the sentiment analysis results.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Set up the Twitter API credentials for dynamic tweet fetching.
4. Run the Django web application to explore the sentiment analysis results.

## Acknowledgments

This project represents our graduation effort, where we dedicated our time and skills to develop a robust sentiment analysis system for World Cup 2022 tweets. We hope you find our work insightful and valuable.

Thank you for your time and interest in our project! 😊
