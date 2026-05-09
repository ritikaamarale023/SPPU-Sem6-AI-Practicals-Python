# Elementary Chatbot in Python

print("===== Welcome to Customer Support Chatbot =====")
print("Type 'bye' to exit\n")

while True:

    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif "price" in user:
        print("Bot: Prices are available on our website.")

    elif "product" in user:
        print("Bot: We offer electronics, clothes, and accessories.")

    elif "delivery" in user:
        print("Bot: Delivery takes 3 to 5 business days.")

    elif "payment" in user:
        print("Bot: We accept UPI, cards, and net banking.")

    elif user == "bye":
        print("Bot: Thank you for visiting!")
        break

    else:
        print("Bot: Sorry, I did not understand your query.")
        