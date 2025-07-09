import streamlit as st
import pickle
from clean import clean_text
import joblib

# Load model and vectorizer
model = joblib.load("../models/logistic_model.pkl")
vectorizer = joblib.load("../models/tfidf_vectorizer.pkl")

# Streamlit UI
st.set_page_config(page_title="Fake News Detector", page_icon="📰")

st.title("📰 Fake News Detection using ML")
st.write("Enter a news statement below and click **Detect** to know if it's Real or Fake.")

user_input = st.text_area("Enter News Content")

if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        if prediction == 1:
            st.success("✅ This looks like a **REAL** news article.")
        else:
            st.error("❌ This seems to be **FAKE** news.")
