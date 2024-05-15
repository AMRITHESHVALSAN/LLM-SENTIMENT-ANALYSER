#frontend code using streamlit

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

#importing functions from the other file
from llm_sentiment import reply_fun
from llm_sentiment import paragraph_sentiment
from llm_sentiment import sent_res

#to cound the number of sentences of each sentiment for each session
if 'positive_count' not in st.session_state:
  st.session_state['positive_count'] = 0
if 'negative_count' not in st.session_state:
  st.session_state['negative_count'] = 0
if 'neutral_count' not in st.session_state:
  st.session_state['neutral_count'] = 0


if 'sentiment_scores' not in st.session_state:
  st.session_state['sentiment_scores'] = []  #creating a list of sentiment scores for a session
s=[]
st.title("LLM Sentiment Analyser 💻")
st.write("")
st.markdown("**Note:** Type in bye to reveal end sentiment analysis report")

user_input = st.text_input("Type in your query: ")

if user_input:
    response = reply_fun(user_input) #taking generated response from LLM
    sentiment = paragraph_sentiment(response) #calculating the sentiment scores
    sent_r= sent_res(sentiment) #finding the sentiment
    st.session_state['sentiment_scores'].append(sentiment)

    if sent_r == 'Positive':
      st.session_state['positive_count'] += 1
    elif sent_r == 'Negative':
      st.session_state['negative_count'] += 1
    else:
      st.session_state['neutral_count'] += 1

    st.markdown("**User :😎**")
    st.write(user_input)
    st.markdown("**Assistant  :🤖**")
    st.write(response)
    st.markdown("**Sentiment 📋**")
    st.write(sent_r)
if user_input.lower() == 'bye':
    st.write("")
    st.write("")
    st.write("")
    st.markdown("**THE SENTIMENT REPORT FOR THIS CHAT SESSION IS PRINTED BELOW**", unsafe_allow_html=True)
    st.write("Positive Sentiment Count:", st.session_state['positive_count'])
    st.write("Negative Sentiment Count:", st.session_state['negative_count'])
    st.write("Neutral Sentiment Count:", st.session_state['neutral_count'])

#creating a pie chart for visualizing the sentiment types in a session
    data = {
  'sentiment': ['Positive', 'Negative', 'Neutral'],
  'count': [st.session_state['positive_count'], st.session_state['negative_count'], st.session_state['neutral_count']]}
    
    fig = px.pie(data, values='count', names='sentiment', title='Sentiment Analysis Results')
    st.plotly_chart(fig)


    st.session_state['positive_count'] = 0
    st.session_state['negative_count'] = 0
    st.session_state['neutral_count'] = 0
#a line chart to plot the sentiment scores
    s = st.session_state['sentiment_scores'].copy()
    st.session_state['sentiment_scores']=[]
    x = [x for x in range(1, len(s) + 1)]
    fig = plt.figure(figsize=(8, 5))
    plt.plot(x,s)  # Plot the data points
    plt.xticks(x)
    # Optional customizations (feel free to adjust these)
    plt.xlabel("Replies from LLM")
    plt.ylabel("Sentiment Score")
    plt.title("Sentiment Scores Over LLM replies")
    plt.grid(True)  # Add gridlines for better readability
    plt.show()
    st.pyplot(fig)

    st.markdown("**Note:** Sentiment scores range from -2(Negative) to +2(Positive) ")
