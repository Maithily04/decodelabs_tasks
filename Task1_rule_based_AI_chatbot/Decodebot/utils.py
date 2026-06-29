"""
=========================================
Utility Functions
File : utils.py
Author : Maithily Bhatt
=========================================
"""

from datetime import datetime
import random


# ----------------------------------------
# Get Current Date & Time
# ----------------------------------------
def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ----------------------------------------
# Generate Greeting
# ----------------------------------------
def get_greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning! ☀️"

    elif hour < 17:
        return "Good Afternoon! 🌤️"

    else:
        return "Good Evening! 🌙"


# ----------------------------------------
# Typing Animation (Text)
# ----------------------------------------
def typing_message():
    messages = [
        "Typing...",
        "Thinking...",
        "Generating response...",
        "Please wait..."
    ]

    return random.choice(messages)


# ----------------------------------------
# Clean User Input
# ----------------------------------------
def clean_text(text):

    text = text.strip()
    text = " ".join(text.split())

    return text


# ----------------------------------------
# Random Welcome Message
# ----------------------------------------
def welcome_message():

    messages = [
        "Hello! 👋 I'm your AI Assistant.",
        "Welcome! 😊 How can I help you today?",
        "Hi there! Ready to chat?",
        "Hello! Ask me anything."
    ]

    return random.choice(messages)


# ----------------------------------------
# Exit Message
# ----------------------------------------
def goodbye_message():

    messages = [
        "Goodbye! 👋",
        "See you again!",
        "Have a wonderful day!",
        "Take care!"
    ]

    return random.choice(messages)


# ----------------------------------------
# Character Counter
# ----------------------------------------
def character_count(text):
    return len(text)


# ----------------------------------------
# Word Counter
# ----------------------------------------
def word_count(text):

    if not text.strip():
        return 0

    return len(text.split())


# ----------------------------------------
# Testing
# ----------------------------------------
if __name__ == "__main__":

    print(get_current_datetime())
    print(get_greeting())
    print(welcome_message())
    print(typing_message())
    print(clean_text("   Hello     World   "))
    print(character_count("Python"))
    print(word_count("Python is awesome"))
    print(goodbye_message())