from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

english_bot = ChatBot("Jarvis")


"""
english_bot.set_trainer(ListTrainer)
english_bot.train([
    "Hi there!",
    "Hello",
])
english_bot.train([
    "Greetings!",
    "Hello",
])
english_bot.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])
"""
english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
    return str(english_bot.get_response(query))


if __name__ == "__main__":
    app.run()
