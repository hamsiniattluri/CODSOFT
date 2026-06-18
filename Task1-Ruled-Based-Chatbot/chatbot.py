import tkinter as tk
from tkinter import scrolledtext
import random
import datetime

# ------------------------------
# Chatbot Response Function
# ------------------------------
def get_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice([
            "Hello!",
            "Hi there!",
            "Hey!"
        ])

    elif "how are you" in user_input:
        return "I am fine. How are you?"

    elif "your name" in user_input:
        return "My name is RuleBot."

    elif "python" in user_input:
        return "Python is a powerful programming language."

    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence."

    elif "date" in user_input:
        return datetime.datetime.now().strftime("Today's date is %d-%m-%Y")

    elif "time" in user_input:
        return datetime.datetime.now().strftime("Current time is %H:%M:%S")

    elif "joke" in user_input:
        return random.choice([
            "Why do programmers love Python? Because it's easy to read!",
            "Why did the computer go to the doctor? It caught a virus!",
            "Why was the Java developer sad? Because he didn't get a class!"
        ])

    elif user_input.startswith("calculate"):
        try:
            expression = user_input.replace("calculate", "").strip()
            answer = eval(expression)
            return f"Answer = {answer}"
        except:
            return "Invalid calculation."

    elif "help" in user_input:
        return """
Available Commands:

hello
how are you
your name
python
ai
date
time
joke
calculate 5+10
help
bye
"""

    elif "bye" in user_input:
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


# ------------------------------
# Send Message Function
# ------------------------------
def send_message():

    user_message = entry_box.get().strip()

    if user_message == "":
        return

    # Show user message
    chat_area.insert(tk.END, "You: " + user_message + "\n")

    # Get bot response
    bot_response = get_response(user_message)

    # Show bot response
    chat_area.insert(tk.END, "Bot: " + bot_response + "\n\n")

    # Save history
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write("You: " + user_message + "\n")
        file.write("Bot: " + bot_response + "\n\n")

    # Clear input box
    entry_box.delete(0, tk.END)

    # Scroll down automatically
    chat_area.see(tk.END)


# ------------------------------
# Main Window
# ------------------------------
root = tk.Tk()
root.title("Advanced Rule Based Chatbot")
root.geometry("700x550")

# Heading
title_label = tk.Label(
    root,
    text="🤖 Rule Based Chatbot",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

# Chat Area
chat_area = scrolledtext.ScrolledText(
    root,
    width=80,
    height=25,
    font=("Arial", 11)
)
chat_area.pack(padx=10, pady=10)

# Welcome Message
chat_area.insert(
    tk.END,
    "Bot: Hello! I am RuleBot.\nType 'help' to see commands.\n\n"
)

# Bottom Frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

# Input Box
entry_box = tk.Entry(
    bottom_frame,
    width=50,
    font=("Arial", 12)
)
entry_box.pack(side=tk.LEFT, padx=5)

# Send Button
send_button = tk.Button(
    bottom_frame,
    text="Send",
    width=15,
    command=send_message
)
send_button.pack(side=tk.LEFT)

# Enter Key Support
entry_box.bind("<Return>", lambda event: send_message())

# Run App
root.mainloop()