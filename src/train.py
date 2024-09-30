
"""
Copyright (c) 2024 Kawsar Alam Foysal

Developed by: Kawsar Alam Foysal
Email: foysalf652@gmail.com
github: iamfoysal
medium: @foysalff
linkedin: kawsaralam101
Created on: 2024-09-30

This is the main file of the project. It contains the primary logic for 
training and running a chatbot using TensorFlow and NLP techniques. 
Please do not use or distribute this code without permission from the author.

Description:
This file initializes and runs the main chatbot interface, 
providing functionalities for training and responding to user input.

"""


from model import create_model
from utils import load_intents, prepare_data, encode_data
import numpy as np


intents = load_intents('data/intents.json')

docs, words, label_list = prepare_data(intents)
X_train, y_train = encode_data(docs, words, label_list)

model = create_model(input_shape=(
    len(X_train[0]),), num_classes=len(label_list))


model.fit(X_train, y_train, epochs=200, batch_size=8)

# Save the model
# model.save('models/chatbot_model.h5')
model.save('models/chatbot_model.keras')

