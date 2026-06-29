"""
=========================================
Chat History Manager
File: chat_history.py
=========================================
"""

import json
import os
from datetime import datetime


class ChatHistory:

    def __init__(self, filename="chat_history.json"):
        self.filename = filename

        # Create file if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump([], file, indent=4)

    # -----------------------------------
    # Load Chat History
    # -----------------------------------
    def load_history(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except:
            return []

    # -----------------------------------
    # Save One Conversation
    # -----------------------------------
    def save_message(self, sender, message):

        history = self.load_history()

        history.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "sender": sender,
            "message": message
        })

        with open(self.filename, "w") as file:
            json.dump(history, file, indent=4)

    # -----------------------------------
    # Get Entire History
    # -----------------------------------
    def get_history(self):
        return self.load_history()

    # -----------------------------------
    # Clear History
    # -----------------------------------
    def clear_history(self):
        with open(self.filename, "w") as file:
            json.dump([], file, indent=4)

    # -----------------------------------
    # Export to Text File
    # -----------------------------------
    def export_txt(self, filename="conversation.txt"):

        history = self.load_history()

        with open(filename, "w") as file:
            for item in history:
                file.write(
                    f"[{item['time']}] "
                    f"{item['sender']}: "
                    f"{item['message']}\n"
                )

        return filename

    # -----------------------------------
    # Delete Last Message
    # -----------------------------------
    def delete_last_message(self):

        history = self.load_history()

        if history:
            history.pop()

            with open(self.filename, "w") as file:
                json.dump(history, file, indent=4)

    # -----------------------------------
    # Total Messages
    # -----------------------------------
    def total_messages(self):
        return len(self.load_history())


# =====================================
# Testing
# =====================================
if __name__ == "__main__":

    chat = ChatHistory()

    chat.save_message("User", "Hello")
    chat.save_message("AI", "Hi! How can I help you?")

    print(chat.get_history())

    print("Total Messages:", chat.total_messages())

    chat.export_txt()

    # Uncomment to test
    # chat.delete_last_message()
    # chat.clear_history()