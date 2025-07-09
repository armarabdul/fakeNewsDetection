# 📰 Fake News Detection Using Machine Learning

This project aims to build a machine learning model that can automatically classify news content as **Real** or **Fake**. It uses Natural Language Processing (NLP) techniques for text preprocessing and training a classifier to detect misinformation.

---

## 🚀 Demo

Try it locally with Streamlit:

```bash
streamlit run streamlit_app/app.py

Project Structure

fake-news-detection-project/
│
├── data/
│   ├── Fake.csv
│   ├── True.csv
│   └── merged_news.csv
│
├── models/
│   ├── logistic_model.pkl
│   ├── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── Fake_News_Detection_Model.ipynb
│
├── streamlit_app/
│   ├── app.py
│   ├── clean.py
│   └── style.css
│
├── README.md
├── requirements.txt
└── .gitignore

Model Overview
Vectorizer: TF-IDF (TfidfVectorizer)

Classifier: Logistic Regression

Libraries Used:

pandas

numpy

nltk

scikit-learn

streamlit

pickle


Dataset
The dataset used in this project is sourced from Kaggle - Fake and Real News Dataset.

Fake.csv — Articles labeled as fake

True.csv — Articles labeled as real

Merged and preprocessed in merged_news.csv


Preprocessing Steps
Lowercasing

Removing punctuation

Tokenization

Stopword removal

Lemmatization

Done using nltk and custom functions in clean.py


Model Training
Vectorized using TF-IDF with top 5000 features

Split into train/test (80/20)

Trained with Logistic Regression

Accuracy, Precision, Recall, and F1 Score reported


Streamlit App Features
Simple UI for news text input

Real-time prediction: Real or Fake

Confidence/probability output

Styled with custom style.css

Requirements
Install all dependencies using:  pip install -r requirements.txt


Future Improvements
Add LSTM or BERT-based deep learning models

Include fake news dataset from Indian news sources

Deploy using Heroku, Render, or AWS

Add news source credibility score

 License
This project is open-source and free to use under the MIT License.

👨‍💻 Author
Armar Abdul
M.Tech Mini Project – MSCS206
Subject: Mini Project with Seminar
Institution: Bearys Institute of technology and management

⭐ If you found this useful, don't forget to star the repo!
