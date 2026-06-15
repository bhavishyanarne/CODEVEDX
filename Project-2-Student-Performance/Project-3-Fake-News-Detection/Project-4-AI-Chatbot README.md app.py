print("=== AI Helpdesk Chatbot ===")
print("Type 'bye' to exit")

while True:

    q = input("\nYou: ").lower()

    if q == "hello":
        print("Bot: Hi! Welcome.")

    elif q == "internship":
        print("Bot: Internship duration is 1 month.")

    elif q == "certificate":
        print("Bot: Complete at least 3 projects to be eligible.")

    elif q == "github":
        print("Bot: Upload all projects to GitHub.")

    elif q == "project":
        print("Bot: There are 5 AI/ML projects available.")

    elif q == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")
