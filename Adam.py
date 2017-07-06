from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json
import logging
import myParser

app = Flask(__name__)

bot = ChatBot("Adam",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand. Please rephrase the question'
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    trainer="chatterbot.trainers.ListTrainer",
    database="botDB/database.db"
)


with open('data.json') as json_data:
    data = json.load(json_data)
for item in data.get("statements"):
    #print(item)
    bot.train(item)

bot.train([
	"Hi",
    "Hi,How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome. How can I help you?",
])

bot.train(
    "chatterbot.corpus.english.greetings"
)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
    response = bot.get_response(query)
    print(response)
    return str(response)

@app.route("/getFormat/<string:query>")
def get_format(query):
	ret = myParser.parseQnA(query)
	return str(ret)
	
if __name__ == "__main__":
    app.run()
