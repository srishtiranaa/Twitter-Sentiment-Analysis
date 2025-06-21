# 🐦 Twitter Sentiment Analysis

This project is a **Twitter Sentiment Analyzer** built using **Streamlit**, **Scikit-learn**, and **MongoDB Atlas**. It allows users to input tweets and instantly analyze whether the sentiment is **positive** or **negative**, using a machine learning model trained on textual data.

---

## 🌟 Features

- 🔍 Real-time sentiment analysis of tweets.
- 💬 One-click sample tweet testing.
- 📊 Sentiment score visualization via bar charts.
- 🧠 Uses pre-trained ML model with TF-IDF vectorization.
- 🗃️ Stores analysis results in MongoDB Atlas.
- 🎨 Aesthetic and user-friendly UI with background image and color-coded feedback.
- 🕒 Displays history of recent analyses.

---

## 🛠️ Tech Stack

| Component    | Technology       |
|--------------|------------------|
| Frontend     | Streamlit        |
| Backend      | Python + MongoDB |
| ML Model     | Scikit-learn     |
| Database     | MongoDB Atlas    |
| Additional   | Joblib, Pandas   |

---

## 📁 Folder Structure

├── app.py # Main Streamlit app
├── trained_model.sav # Pre-trained classifier
├── tfidf_vectorizer.pkl # TF-IDF vectorizer for preprocessing
├── package.json # Node.js config (optional backend use)
├── .gitattributes # Git LFS config for large files
├── README.md # Project documentation



---

## ⚙️ Setup & Usage

### 1. Clone the Repository


git clone https://github.com/srishtiranaa/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis

### 2. Install Python Dependencies

Make sure you have Python 3.8+ and pip installed.
pip install streamlit scikit-learn pandas pymongo joblib

### 3. Launch the App

streamlit run app.py

### 4. Launch the App

streamlit run app.py
The app will open in your default browser at http://localhost:8501.

## 💾 MongoDB Atlas Setup

The app is connected to MongoDB using a hardcoded connection string inside app.py.
Replace the connection URI with your own MongoDB credentials for secure deployment:
client = pymongo.MongoClient("your_mongodb_connection_string")

## 📦 Git Large File Support
This repo uses Git LFS for model and vectorizer files.
To enable:
          git lfs install
          git lfs pull


## 🔮 Model Details
Text Preprocessing: TF-IDF Vectorization
Classifier: Trained using Scikit-learn (e.g., Logistic Regression / Naive Bayes)
Output: Binary sentiment (Positive 😊 or Negative 😞)
Confidence: Displayed via probabilities in a bar chart


## 🚀 Future Enhancements
Handle emojis, hashtags, and mentions more effectively.
Add a third "Neutral" sentiment class.
Provide downloadable reports.
Add user login and personalized history.


### 📄 License
This project is open source and available under the MIT License.
