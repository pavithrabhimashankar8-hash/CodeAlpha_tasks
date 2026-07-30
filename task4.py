def get_bot_response(user_input):
    """
    Core logic: Takes user input and returns a predefined response 
    based on basic 'if-elif-else' rules.
    """
    
    # --- Step 1: Normalize user input ---
    # Convert input to lowercase and strip leading/trailing spaces.
    # This ensures that "Hello", "hello", and "  hElLo " are treated the same.
    cleaned_input = user_input.lower().strip()

    # --- Step 2: Define Rule-Based Responses (if-elif-else) ---
    
    # Match against standard greetings
    if cleaned_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"

    # Match against standard status inquiries
    elif cleaned_input in ["how are you", "how's it going", "how are things"]:
        return "I am fine, thank you for asking! How about you?"
    
    # Additional simple knowledge base rule (bonus)
    elif cleaned_input in ["what is your name", "who are you"]:
        return "I am the CodeAlpha Basic Chatbot, a simple AI experiment."
    
    # Additional simple knowledge base rule (bonus)
    elif cleaned_input in ["what can you do", "help"]:
        return "I can respond to basic greetings like 'hello', ask 'how are you', tell you my name, or say 'goodbye'."

    # Match against exit commands
    elif cleaned_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day. (Exiting chatbot...)"

    # --- Step 3: Default "Catch-All" Response ---
    # If the bot doesn't understand the input, provide a polite fallback.
    else:
        return "I'm sorry, I don't understand that yet. I'm a basic chatbot still learning new phrases!"

def start_chatbot():
    """
    Main function to run the interactive chatbot loop.
    Fulfills the 'loops' and 'input/output' key concepts.
    """
    
    print("\n--- CodeAlpha Basic Chatbot ---")
    print("Welcome! Type 'hello' to begin, 'help' for options, or 'bye' to exit.")
    
    # --- Step 4: The Game/Chat Loop (while loop) ---
    running = True
    while running:
        try:
            # Step 5: Input/Output (input from user)
            user_message = input("\nYou: ")
            
            # Step 6: Process input and get response (function call)
            bot_reply = get_bot_response(user_message)
            
            # Step 7: Input/Output (output response)
            print(f"Bot: {bot_reply}")

            # Step 8: Handle Exit Condition
            # If the bot's response contained the shutdown message, end the loop.
            if "(Exiting chatbot...)" in bot_reply:
                running = False

        except (KeyboardInterrupt, EOFError):
            # Handle abrupt exit (like Ctrl+C in terminal)
            print("\n\nAbruptly exiting. Goodbye!")
            running = False
            
    print("\n--- Chat session ended. ---")

# --- Step 9: Start the Application ---
if __name__ == "__main__":
    start_chatbot()