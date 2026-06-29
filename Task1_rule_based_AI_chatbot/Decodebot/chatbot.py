"""
=========================================
DecodeBot
File : chatbot.py
Author : Maithily Bhatt
=========================================
"""

import random
from datetime import datetime


class ChatBot:
    def __init__(self):
        self.memory = {}

        self.jokes = [
            "Why don't programmers like nature? It has too many bugs!",
            "Why did the computer go to the doctor? Because it caught a virus!",
            "Why was the Python developer calm? Because they knew how to handle exceptions!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]

        self.facts = [
            "Honey never spoils.",
            "Bananas are berries, but strawberries are not.",
            "Octopuses have three hearts.",
            "A day on Venus is longer than a year on Venus.",
            "The Eiffel Tower grows a little taller in summer due to heat expansion."
        ]

    # ----------------------------------------
    # Generate Response
    # ----------------------------------------
    def get_response(self, user_input):

        message = user_input.strip()
        text = message.lower()

        # Greetings
        if text in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
            return "Hello! 👋 How can I help you today?"

        # Name Memory
        elif "my name is" in text:
            name = message[message.lower().find("my name is") + len("my name is"):].strip()

            if name:
                self.memory["name"] = name.title()
                return f"Nice to meet you, {name.title()}!"
            else:
                return "I didn't catch your name."

        elif "what is my name" in text:
            if "name" in self.memory:
                return f"Your name is {self.memory['name']}."
            else:
                return "I don't know your name yet. Tell me by saying 'My name is ...'."

        # About Bot
        elif "your name" in text:
            return "I'm DecodeBot, your AI chatbot."

        elif "who created you" in text:
            return "I was created using Python."

        elif "how are you" in text:
            return "I'm doing great! Thanks for asking."

        elif "where are you from" in text:
            return "I'm from the digital world."

        # Time & Date
        elif "time" in text:
            return datetime.now().strftime("Current Time: %I:%M:%S %p")

        elif "date" in text:
            return datetime.now().strftime("Today's Date: %d-%m-%Y")

        # Joke
        elif "joke" in text:
            return random.choice(self.jokes)

        # Fact
        elif "fact" in text:
            return random.choice(self.facts)

        # Simple Knowledge
        elif "python" in text:
            return "Python is a popular programming language used in AI, web development, automation, and data science."

        elif "ai" in text or "artificial intelligence" in text:
            return "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."

        elif "machine learning" in text:
            return "Machine Learning is a branch of AI where computers learn from data."

        elif "thank" in text:
            return "You're welcome! 😊"

        elif "bye" in text or "exit" in text:
            if "name" in self.memory:
                return f"Goodbye, {self.memory['name']}! Have a wonderful day!"
            return "Goodbye! Have a wonderful day!"

        # Basic Math
        elif text.startswith("calculate"):
            try:
                expression = message[9:].strip()
                answer = eval(expression)
                return f"The answer is {answer}"
            except Exception:
                return "Sorry, I couldn't calculate that."

        # Unknown
        else:
            return (
                "I'm sorry, I don't understand that yet.\n"
                "Try asking about:\n"
                "- Time\n"
                "- Date\n"
                "- Tell me a joke\n"
                "- Tell me a fact\n"
                "- Python\n"
                "- AI\n"
                "- My name is ..."
            )


# ----------------------------------------
# Run Directly
# ----------------------------------------
if __name__ == "__main__":

    bot = ChatBot()

    print("=" * 45)
    print("🤖 DecodeBot AI")
    print("Type 'bye' to exit.")
    print("=" * 45)

    while True:

        user = input("You : ")

        reply = bot.get_response(user)

        print("Bot :", reply)

        if user.lower() in ["bye", "exit"]:
            break