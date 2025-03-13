import json

def get_bot_response(user_message):
    responses = {
        "hello": "Hello! How can I help you today?",
        "tell me about [place]": "[Place] is a wonderful location! What would you like to know?",
        "bye": "Goodbye! Have a great day!"
    }
    
    return responses.get(user_message, "I'm sorry, I don't understand that question.")

def main():
    print("Welcome to the chatbot! You can ask me questions or type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break
        
        bot_response = get_bot_response(user_input)
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()