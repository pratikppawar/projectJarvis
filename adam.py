from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot

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
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
)


<<<<<<< HEAD
with open('statements.json') as json_data:
    d = json.load(json_data)
    #print(d.get("statements"))
for item in data:
    bot.train(item)
=======
with open('data.json') as json_data:
    d = json.load(json_data)
    #print(d.get("statements"))
>>>>>>> f763bc1179ec07a3d76c521172ca17c63ddd8564

bot.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome. How can I help you?",
])
<<<<<<< HEAD

=======
for item in d.get("statements"):
	bot.train(item)
>>>>>>> f763bc1179ec07a3d76c521172ca17c63ddd8564

bot.train(
    "chatterbot.corpus.english.greetings"
)

#getTraningData

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
