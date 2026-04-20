import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')

data = """
Hello! Welcome to CodTech AI Chatbot.
Artificial Intelligence is the simulation of human intelligence by machines.
Machine Learning is a subset of AI.
Python is a popular programming language.
Natural Language Processing helps computers understand human language.
Chatbots are used in customer service.
"""

sent_tokens = nltk.sent_tokenize(data)
lemmer = nltk.stem.WordNetLemmatizer()

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    return [lemmer.lemmatize(word) for word in tokens if word.isalnum()]

greet_inputs = ("hello", "hi", "hey")
greet_responses = ["Hello!", "Hi there!", "Hey!"]

def greeting(user_input):
    for word in user_input.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)

def chatbot_response(user_input):
    sent_tokens.append(user_input)

    vectorizer = TfidfVectorizer(tokenizer=preprocess)
    vectors = vectorizer.fit_transform(sent_tokens)

    similarity = cosine_similarity(vectors[-1], vectors)
    idx = similarity.argsort()[0][-2]

    sent_tokens.pop()

    return sent_tokens[idx]

print("🤖 Chatbot started (type 'bye' to exit)")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye!")
        break

    elif greeting(user_input) is not None:
        print("Bot:", greeting(user_input))

    else:
        print("Bot:", chatbot_response(user_input))
