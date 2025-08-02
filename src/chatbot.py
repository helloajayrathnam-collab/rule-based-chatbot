import re
from datetime import datetime

def chatbot():
    print("🤖 Chatbot: Hello! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").lower()

        if user_input in ['exit', 'quit', 'bye']:
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("🤖 Chatbot: Hello there! How can I help you today?")
        elif 'your name' in user_input:
            print("🤖 Chatbot: I’m ChatBot, your virtual assistant.")
        elif 'how are you' in user_input:
            print("🤖 Chatbot: I'm doing well, thank you!")
        elif 'time' in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: The current time is {now}.")
        elif re.search(r'weather.*\?', user_input):
            print("🤖 Chatbot: I can't check the weather right now.")
        elif 'help' in user_input:
            print("🤖 Chatbot: You can ask me the time, greetings, or questions.")
        else:
            print("🤖 Chatbot: I'm sorry, I didn't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

