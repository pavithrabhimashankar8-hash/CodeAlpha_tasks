print("=" * 50)
print("         FAQ CHATBOT")
print("=" * 50)

faq = {
    "hello": "Hello! Welcome to CodeAlpha AI Chatbot.",
    "hi": "Hi! How can I help you?",
    "what is ai": "AI means Artificial Intelligence.",
    "python": "Python is a simple and powerful programming language.",
    "codealpha": "CodeAlpha provides internship programs for students.",
    "bye": "Thank you! Have a nice day."
}

while True:
    user = input("\nYou: ").lower()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    elif user in faq:
        print("Bot:", faq[user])

    else:
        print("Bot: Sorry, I don't know the answer.")