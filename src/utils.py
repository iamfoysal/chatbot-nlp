from .preprocess import preprocess_text
import numpy as np
import json


def load_intents(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data


def prepare_data(intents):
    words = []
    labels = []
    docs = []
    label_list = []

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            tokens = preprocess_text(pattern)
            words.extend(tokens)
            docs.append((tokens, intent['tag']))

        if intent['tag'] not in label_list:
            label_list.append(intent['tag'])

    words = sorted(set(words))
    label_list = sorted(label_list)

    return docs, words, label_list


def encode_data(docs, words, label_list):
    training = []
    output = []

    for doc in docs:
        bag = [1 if word in doc[0] else 0 for word in words]
        label_index = label_list.index(doc[1])
        training.append(bag)
        output.append(label_index)

    return np.array(training), np.array(output)
