# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: UNNATI SINGH

*INTERN ID*: CTIS8018 

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

AI Chatbot Project

Overview

This project is a simple AI chatbot built using Python. It runs on a command-line interface and can respond to basic user queries using Natural Language Processing (NLP). The chatbot matches user input with a predefined knowledge base and returns the most relevant response.

Platform and Development Environment

The chatbot was developed on a Windows system using Visual Studio Code as the code editor. The integrated terminal in Visual Studio Code was used to run the Python script and manage dependencies. The project files are stored locally and can be executed directly from the project folder.

Programming Language

- Python 3.x

Python was used because of its simplicity and strong support for NLP libraries.

Libraries and Tools Used

- NLTK (Natural Language Toolkit): Used for text processing tasks such as tokenization and lemmatization.
- Scikit-learn: Used to implement TF-IDF vectorization and cosine similarity for matching user queries.
- Random (built-in): Used to generate random greeting responses.

All required libraries were installed using pip in the terminal.

Installation and Setup

To run this project, the following steps were performed:

1. Open the terminal in the project folder.

2. Install required libraries:
   pip install nltk scikit-learn

3. Download necessary NLTK data:
   python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('punkt_tab')"

4. Run the chatbot script:
   python chatbot.py

How the Chatbot Works

The chatbot uses a predefined text dataset stored inside the Python file. When a user enters a message, the chatbot processes the input using NLTK. The text is tokenized and cleaned before being converted into numerical form using TF-IDF vectorization. Cosine similarity is then applied to compare the user input with the dataset. The most similar sentence is selected and returned as the chatbot’s response.

The chatbot also includes a simple greeting detection system. If the user enters words like "hello" or "hi", it responds with a greeting message.

Project Structure

- chatbot.py: Main Python script containing chatbot logic and dataset
- README.md: Documentation file

Usage

After running the script, the chatbot starts in the terminal. The user can type messages and receive responses instantly. To end the conversation, the user can type "bye", which stops the program.

Notes

This chatbot is a basic implementation and works only with the provided dataset. The responses depend on the data written in the code. The project can be extended by adding more data, improving response handling, or building a graphical user interface.

Author

Unnati Singh
