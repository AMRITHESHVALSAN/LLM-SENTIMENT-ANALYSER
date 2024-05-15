import google.generativeai as genai
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import matplotlib.pyplot as plt

import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially Google api key)


genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')
analyzer = SentimentIntensityAnalyzer() #model initialization


#function to generate LLM response
def reply_fun(query):
    default_message = "I'm unable to understand your query right now. Please rephrase or try a different query."

    try:
        # Attempt to generate content using the model
        response = model.generate_content(query).text

        # If response is a valid text object, return it
        if isinstance(response, str):
            return response.strip()  # Remove potential leading/trailing whitespace

        # If response is not text, handle the error gracefully
        else:

            return default_message

    except Exception as e:
        # Catch any other potential exceptions for robustness
    
        return default_message

#function to generate the sentiment scores 
def paragraph_sentiment(paragraph):
    """
    This function analyzes the sentiment of a paragraph using sentence-level analysis.
    """
    sentences = paragraph.split(". ")  # Split into sentences
    sentiment_scores = []
    analyzer = SentimentIntensityAnalyzer()

    for sentence in sentences:
        score = analyzer.polarity_scores(sentence)
        sentiment_scores.append(score)
    scores = analyzer.polarity_scores(paragraph)
    # Implement your desired logic for combining sentiment scores (e.g., averaging, voting)
    overall_sentiment = (sum(score['compound'] for score in sentiment_scores) + scores['compound']) / len(sentiment_scores)

    return overall_sentiment

#function to print the sentiment 
def sent_res(num):
    
    if num <= -0.1:
        sentiment_text = "Negative"
        
    elif num >= 0.2:
        sentiment_text = "Positive"
       
    else:
        sentiment_text = "Neutral"
        
    return sentiment_text