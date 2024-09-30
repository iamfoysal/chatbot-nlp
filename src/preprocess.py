import json
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens


def load_intents(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data
