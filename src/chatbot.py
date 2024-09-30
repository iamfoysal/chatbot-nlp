import numpy as np
import tensorflow as tf
from src.utils import preprocess_text, load_intents
from tensorflow.keras.models import load_model

# Load trained model and necessary data
# model = load_model('models/chatbot_model.h5')

model = load_model('models/chatbot_model.keras')
intents = load_intents('data/intents.json')
words = sorted(set([word for intent in intents['intents']
               for pattern in intent['patterns'] for word in preprocess_text(pattern)]))
label_list = [intent['tag'] for intent in intents['intents']]


def predict_class(input_text):
    tokens = preprocess_text(input_text)
    bag = [1 if word in tokens else 0 for word in words]
    prediction = model.predict(np.array([bag]))[0]
    class_index = np.argmax(prediction)
    return label_list[class_index]


def get_response(tag):
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return np.random.choice(intent['responses'])


def chatbot_response(input_text):
    tag = predict_class(input_text)
    return get_response(tag)
