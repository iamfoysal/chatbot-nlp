chatbot_project/
│
├── data/
│   └── intents.json         # Example data with intents for training (text, labels)
│
├── models/
│   └── chatbot_model.h5     # Saved trained model
│
├── src/
│   ├── __init__.py          # Optional, makes 'src' a Python module
│   ├── model.py             # Model creation and training script
│   ├── preprocess.py        # Data preprocessing script
│   ├── train.py             # Script for training the model
│   ├── chatbot.py           # Chatbot response logic
│   └── utils.py             # Utility functions (e.g., loading data)
│
├── chatbot.py               # Main script to run the chatbot
└── requirements.txt         # Python dependencies
