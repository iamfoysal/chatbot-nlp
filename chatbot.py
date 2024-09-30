
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



from src.chatbot import chatbot_response

print("Chatbot is running. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot_response(user_input)
    print(f"Bot: {response}")
    
