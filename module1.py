import re
import wikipediaapi

# Initialize Wikipedia API with your user agent
wiki = wikipediaapi.Wikipedia('Areola/1.0 (cleefrookie@gmail.com)', 'en')

# Predefined Q&A dictionary
responses = {
    "hi": "Hello! what's good my man?",
    "how are you": "I'm just a program, but thanks for asking! How can I assist you today?",
    "what is the weather like?": "I ain't got a window, but tell me your location and I'll guess......or not",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "who made you?": "I was brought to life by cleef rookie and Grok AI, a team of developers and AI enthusiasts. They created me to assist and entertain users like you!",
    "what is your name?": "I am Areola, your friendly neighborhood AI assistant!",
    "what can you do?": "I can answer questions, tell jokes, provide information, and assist with various tasks. Just ask away!",
}

def get_wikipedia_summary(query):
    page = wiki.page(query)
    if page.exists():
        # Remove Wikipedia references like [1], [2], etc.
        summary = re.sub(r'\[.*?\]', '', page.summary)
        return summary[:500] + "..."  # Limit to 500 chars for brevity
    else:
        return f"Sorry, I couldn't find anything on Wikipedia about '{query}'."

def chatbot_response(user_input):
    # Check for predefined responses (case-insensitive)
    user_input = user_input.lower().strip()
    for question, answer in responses.items():
        if user_input in question or question in user_input:
            return answer
    # If no predefined match, try Wikipedia
    return get_wikipedia_summary(user_input)

def main():
    print("Welcome to Areola, your upgraded bot, type 'quit' to bounce.", flush=True)
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Areola: Goodbye! Peace out!")
            break
        response = chatbot_response(user_input)
        print(f"Areola: {response}")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")