from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

Hugo = ChatBot(name="Hugo",
                      read_only = False,
                      logic_adapters = ["chatterbot.logic.BestMatch"],
                      storage_adapter = "chatterbot.storage.SQLStorageAdapter")

while(True):
    user_input = input()
    if(user_input == 'quit'):
        break
    response = Hugo.get_response(user_input)
    print(response)
