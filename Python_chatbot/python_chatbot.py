import random
from datetime import datetime

print("🤖 SmartBot 2.0: Hello! I'm your upgraded assistant. Type 'bye' anytime to exit.\n")

# Predefined data
greetings = ["hi", "hello", "hey", "hola"]
farewells = ["bye", "exit", "quit", "goodbye"]
thanks_keywords = ["thank", "thanks", "thank you"]
jokes = [
    "😂 Why do robots love summer? Because they have fans!",
    "💡 I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep.'",
    "🖥️ I would tell you a UDP joke, but you might not get it."
]
fallback_responses = [
    "🤔 Hmm... I didn’t get that. Try asking in another way!",
    "📚 I'm still learning. Can you rephrase that?",
    "🧠 Interesting... Can you tell me more?",
    "🤖 Sorry, I don't have a programmed response for that yet."
]

def get_response(user_input):
    user_input = user_input.lower().strip()

    if any(greet in user_input for greet in greetings):
        return "👋 Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "😊 I'm functioning perfectly! How about you?"

    elif "your name" in user_input or "who are you" in user_input:
        return "🤖 I'm SmartBot 2.0 — your chat buddy!"

    elif "help" in user_input:
        return "🛠️ I can chat, tell jokes, show date/time, and more. Just ask!"

    elif any(word in user_input for word in thanks_keywords):
        return "🙏 You're welcome! Always happy to help."

    elif "weather" in user_input:
        return "🌤️ I can’t fetch live weather yet, but I hope it’s lovely where you are!"

    elif "time" in user_input:
        now = datetime.now().strftime('%H:%M:%S')
        return f"⏰ The current time is {now}"

    elif "date" in user_input:
        today = datetime.now().strftime('%A, %B %d, %Y')
        return f"📅 Today is {today}"

    elif "joke" in user_input:
        return random.choice(jokes)

    elif any(farewell in user_input for farewell in farewells):
        return "👋 Goodbye! Take care and see you next time."

    else:
        return random.choice(fallback_responses)

# Chat loop
while True:
    user_input = input("You: ")
    response = get_response(user_input)

    print(f"SmartBot: {response}")
    if response.startswith("👋 Goodbye"):
        break
