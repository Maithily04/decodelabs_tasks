"""
=========================================================
DecodeBot
File : gui.py
Author : Maithily Bhatt
=========================================================
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox

from chatbot import ChatBot
from chat_history import ChatHistory


class ChatGUI:

    def __init__(self):

        # -----------------------------
        # Objects
        # -----------------------------
        self.bot = ChatBot()
        self.history = ChatHistory()

        # -----------------------------
        # Main Window
        # -----------------------------
        self.root = tk.Tk()

        self.root.title("🤖 DecodeBot")
        self.root.geometry("900x650")
        self.root.minsize(700, 500)

        self.bg_color = "#202123"
        self.chat_bg = "#343541"
        self.user_color = "#0B93F6"
        self.bot_color = "#444654"
        self.text_color = "white"

        self.root.configure(bg=self.bg_color)

        # -----------------------------
        # Header
        # -----------------------------
        header = tk.Label(
            self.root,
            text="🤖 DecodeBot",
            font=("Arial", 22, "bold"),
            bg=self.bg_color,
            fg="white",
            pady=15
        )

        header.pack(fill="x")

        # -----------------------------
        # Chat Area
        # -----------------------------
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg=self.chat_bg,
            fg="white",
            insertbackground="white",
            bd=0,
            padx=10,
            pady=10
        )

        self.chat_area.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        self.chat_area.config(state=tk.DISABLED)

        # -----------------------------
        # Bottom Frame
        # -----------------------------
        bottom_frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        bottom_frame.pack(
            fill="x",
            padx=15,
            pady=10
        )

        # -----------------------------
        # Message Entry
        # -----------------------------
        self.entry = tk.Entry(
            bottom_frame,
            font=("Arial", 13),
            width=60
        )

        self.entry.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=(0, 10)
        )

        self.entry.focus()

        # -----------------------------
        # Send Button
        # -----------------------------
        self.send_button = tk.Button(
            bottom_frame,
            text="Send",
            font=("Arial", 11, "bold"),
            bg="#10A37F",
            fg="white",
            width=10
        )

        self.send_button.pack(side=tk.LEFT)

        # -----------------------------
        # Clear Button
        # -----------------------------
        self.clear_button = tk.Button(
            bottom_frame,
            text="Clear",
            font=("Arial", 11, "bold"),
            bg="#EF4444",
            fg="white",
            width=10
        )

        self.clear_button.pack(side=tk.LEFT, padx=5)

        # -----------------------------
        # Exit Button
        # -----------------------------
        self.exit_button = tk.Button(
            bottom_frame,
            text="Exit",
            font=("Arial", 11, "bold"),
            bg="#555555",
            fg="white",
            width=10
        )

        self.exit_button.pack(side=tk.LEFT)

        # -----------------------------
        # Button Commands
        # -----------------------------
        self.send_button.config(command=self.send_message)
        self.clear_button.config(command=self.clear_chat)
        self.exit_button.config(command=self.close_app)

        # Press Enter to Send
        self.entry.bind("<Return>", self.send_message)

        # -----------------------------
        # Welcome Message
        # -----------------------------
        self.display_message(
            "Bot",
            "Hello! 👋 I'm your AI assistant. How can I help you today?"
        )

        # -----------------------------
        # Load Previous Chat History
        # -----------------------------
        self.load_chat_history()

    # =====================================================
    # Display Message
    # =====================================================
    def display_message(self, sender, message):

        self.chat_area.config(state=tk.NORMAL)

        if sender == "You":
            self.chat_area.insert(
                tk.END,
                f"\n🧑 You:\n{message}\n\n"
            )
        else:
            self.chat_area.insert(
                tk.END,
                f"\n🤖 Bot:\n{message}\n\n"
            )

        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    # =====================================================
    # Load Previous Messages
    # =====================================================
    def load_chat_history(self):

        history = self.history.get_history()

        if not history:
            return

        self.chat_area.config(state=tk.NORMAL)

        self.chat_area.delete("1.0", tk.END)

        for item in history:

            sender = item["sender"]
            message = item["message"]

            if sender == "User":
                self.chat_area.insert(
                    tk.END,
                    f"\n🧑 You:\n{message}\n\n"
                )

            else:
                self.chat_area.insert(
                    tk.END,
                    f"\n🤖 Bot:\n{message}\n\n"
                )

        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    # =====================================================
    # Send Message
    # =====================================================
    def send_message(self, event=None):

        user_message = self.entry.get().strip()

        if user_message == "":
            return

        # Display User Message
        self.display_message("You", user_message)

        # Save User Message
        self.history.save_message("User", user_message)

        # Clear Entry Box
        self.entry.delete(0, tk.END)

        # Get Bot Response
        bot_reply = self.bot.get_response(user_message)

        # Display Bot Response
        self.display_message("Bot", bot_reply)

        # Save Bot Response
        self.history.save_message("Bot", bot_reply)

    # =====================================================
    # Clear Chat
    # =====================================================
    def clear_chat(self):

        answer = messagebox.askyesno(
            "Clear Chat",
            "Do you want to clear the chat history?"
        )

        if answer:

            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.delete("1.0", tk.END)
            self.chat_area.config(state=tk.DISABLED)

            self.history.clear_history()

            self.display_message(
                "Bot",
                "Chat history cleared successfully!"
            )

    # =====================================================
    # Close Application
    # =====================================================
    def close_app(self):

        answer = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        )

        if answer:
            self.root.destroy()

    # =====================================================
    # Run GUI
    # =====================================================
    def run(self):
        self.root.mainloop()        
