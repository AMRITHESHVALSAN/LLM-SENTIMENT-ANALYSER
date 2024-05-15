# LLM-SENTIMENT-ANALYSER USING GOOGLE GEMINI | NLP

This is an end to end LLM project based on Google Gemini and Streamlit. We are building a system that can analyse the LLM response. User asks questions in a natural language and the LLM replies.
These replies will be analysed and the sentiment of these response will be displayed.
The response will be divided into 3 categories - Positive, Negative and Neutral

## PROJECT HIGHLIGHTS 

The gemini model is imported and made to work using the Google API key
The user queries are entered and the LLM produces the response
The sentiment scores of these responses are calculated using NLP and the compound score is taken
The sentiment is then classified into categories.
At the end of each session the sentiment analyser report is given for each session along with line graph of compound scores and pie chart of type of sentiments for each session is produced.
  ### Google Gemini (model : gemini-pro)
  ### SentimentIntensityAnalyzer from NLTK
  ### Streamlit for UI

## Project Structure
  * Frontend.py: The main Streamlit application script.
  * Backend_LLM.py: This has all the sentiment analyser and LLM coding
  * .env: Configuration file for storing your Google API key.
  * Screenshots of the GUI also given
 
