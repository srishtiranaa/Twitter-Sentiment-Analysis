# 🐦 Twitter Sentiment Analysis

This project is a **Twitter Sentiment Analyzer** built with **Streamlit**, **Scikit-learn**, and **MongoDB Atlas**. It uses a pre-trained machine learning model and a TF-IDF vectorizer to classify tweets as Positive or Negative based on their content.

## 🚀 Features

- 📊 Real-time sentiment prediction on user-entered tweets
- 💬 Sample tweet buttons to test the model instantly
- 📈 Probability score chart visualization for sentiment confidence
- 🧠 ML model (trained offline) and vectorizer used for inference
- 🗃️ MongoDB Atlas integration to store and retrieve recent analysis
- 🎨 Beautiful UI with a custom background and sentiment color indicators
- 📚 Built-in analysis history to track recent predictions

## 🛠️ Technologies Used

- **Python** (Streamlit, Pandas, Scikit-learn, Joblib, Pymongo)
- **JavaScript/Node.js** (Express, Mongoose - for optional backend API handling)
- **MongoDB Atlas** - for storing tweet analysis logs
- **Machine Learning** - TF-IDF + Classifier
- **Streamlit** - for the interactive web interface

## 📁 Project Structure

├── app.py # Main Streamlit application
├── trained_model.sav # Pre-trained ML model
├── tfidf_vectorizer.pkl # Fitted TF-IDF vectorizer
├── package.json # Node.js backend (optional)
├── .gitattributes # Git LFS config for model/binary files
├── README.md # Project documentation


## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/srishtiranaa/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis


## 2.**Install Python dependencies**

pip install -r requirements.txt

## 3.Run the Streamlit app

streamlit run app.py

## 🧪 **Model Details**
Vectorizer: TF-IDF

Classifier: Trained using Scikit-learn (likely Logistic Regression or similar)

Input: Raw tweet text

Output: Sentiment class (Positive/Negative) with probability scores

## 📦 **Git LFS**
Large files like .sav and .pkl are tracked using Git LFS.

## Make sure to run:
git lfs install


## ✨ **Future Improvements**
Add emoji handling and stopword cleaning in preprocessing

Deploy on cloud (Streamlit Cloud, Render, or Heroku)

Support for Neutral sentiment

Add authentication for saving personalized history

📄** License**
This project is licensed under the MIT License.
