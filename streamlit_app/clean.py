# clean.py
import re
import string
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.data.path.append(os.path.join(os.path.dirname(__file__), "../nltk_data"))

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = re.findall(r"\b\w+\b", text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return " ".join(words)
