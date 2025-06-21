import streamlit as st
import joblib
import pymongo


# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://apple:toothpaste@big-data.ktb9yjz.mongodb.net/?retryWrites=true&w=majority&appName=Big-Data")

# Access the database
db = client['Analysis']

# Access the users collection
users_collection = db['test1']

import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer


# Load your trained model and vectorizer
model = joblib.load("trained_model.sav")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Initialize session state for recent analyses
if "history" not in st.session_state:
    st.session_state.history = []



vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Initialize session state for recent analyses
if "history" not in st.session_state:
    st.session_state.history = []

# Sample tweets
sample_tweets = [
    "I love the new features in this update!",
    "This is the worst experience I've ever had.",
    "Not sure how I feel about this product.",
    "Absolutely amazing service, 10/10!",
    "Totally disappointed with the support.",
]

# Streamlit config
st.set_page_config(page_title="Twitter Sentiment Analyzer", page_icon="🐦", layout="centered")

# App title
st.markdown("<h1 style='text-align: center; color: #00008B;'>🐦 Twitter Sentiment Analyzer</h1>", unsafe_allow_html=True)

# ...existing code...

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images8.alphacoders.com/109/1093606.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Sample tweet buttons
st.markdown("*Try a sample tweet:*")
cols = st.columns(len(sample_tweets))
for i, tweet in enumerate(sample_tweets):
    if cols[i].button("💬", key=f"sample_{i}"):
        st.session_state.tweet_input = tweet

# Input text box
tweet = st.text_area("Enter a tweet to analyze sentiment:", key="tweet_input", height=120)

# Predict and display sentiment
if st.button("🔍 Analyze Sentiment"):
    if tweet.strip() == "":
        st.warning("Please enter a tweet.")
    else:
        # Vectorize and predict
        tweet_vec = vectorizer.transform([tweet])
        prediction = model.predict(tweet_vec)[0]
        probas = model.predict_proba(tweet_vec)[0]

        # Determine sentiment
        sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"
        color = "#D4EDDA" if prediction == 1 else "#F8D7DA"
        text_color = "#155724" if prediction == 1 else "#721C24"

        # Save in history
        st.session_state.history.insert(0, {"tweet": tweet, "sentiment": sentiment, "proba": probas.tolist()})
        st.session_state.history = st.session_state.history[:5]  # keep last 5

        # Show sentiment result
        st.markdown(
            f"<div style='background-color: {color}; padding: 20px; border-radius: 10px; text-align: center;'>"
            f"<h3 style='color: {text_color};'>Sentiment: {sentiment}</h3></div>",
            unsafe_allow_html=True
        )

        # Show bar chart
        st.markdown("### 🔢 Sentiment Scores")
        df_score = pd.DataFrame({
            'Sentiment': ['Negative', 'Positive'],
            'Probability': probas
        })
        st.bar_chart(df_score.set_index("Sentiment"))
       

        # Save analysis result to MongoDB Atlas
        users_collection.insert_one({
            "tweet": tweet,
            "sentiment": sentiment,
            "probabilities": probas.tolist()
        })

# Display recent analysis
if st.session_state.history:
    st.markdown("### 🕒 Recent Analyses")
    for item in st.session_state.history:
        color = "#ED93E7" if "Positive" in item["sentiment"] else "#E15561"
        st.markdown(
            f"<div style='background-color: {color}; padding: 10px; border-radius: 10px; margin-bottom:10px;'>"
            f"<b>Tweet:</b> {item['tweet']}<br><b>Sentiment:</b> {item['sentiment']}</div>",
            unsafe_allow_html=True
        )

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🔍 Made with Streamlit | Sentiment Analysis using ML</p>", unsafe_allow_html=True)