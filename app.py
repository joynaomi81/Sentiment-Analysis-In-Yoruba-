# app.py

import streamlit as st
import joblib
import re

# --- Load trained model and vectorizer ---
nb_model = joblib.load('yoruba_sentiment_nb_model.pkl')
tfidf = joblib.load('yoruba_tfidf_vectorizer.pkl')

# --- Text preprocessing function ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text)  # Keep Yoruba letters
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# --- Prediction function ---
def predict_sentiment(text):
    cleaned_text = clean_text(text)
    text_vector = tfidf.transform([cleaned_text])
    prediction = nb_model.predict(text_vector)[0]
    return prediction

# --- Streamlit UI ---
st.title("📝 Yoruba Sentiment Analysis")
st.write("Enter Yoruba text below to predict its sentiment (Positive, Neutral, Negative).")

user_input = st.text_area("Type your text here:")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        sentiment = predict_sentiment(user_input)
        st.success(f"Predicted Sentiment: **{sentiment}**")
