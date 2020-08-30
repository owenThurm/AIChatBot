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

trainer_bot = ChatBot(name="trainer",
                      read_only = False,
                      logic_adapters = ["chatterbot.logic.BestMatch"],
                      storage_adapter = "chatterbot.storage.SQLStorageAdapter")


conversation_1 = [

"""
	Ayo How you been
""", """
	Just chilling, not doing anything cuz of this virus lol, not worried about it I’m just worried about how crazy people are being about it
	How have you been?
""", """
	Yeah fr people been freakin
	Toilet paper and shit lmao
	Doing good bro at the airport rn coming back from dc
""", """
	There we go man don’t catch corona, Boston is all over that virus rn
	And how was DC?
""", """
	Oh yeah man that’s why I was in dc I got kicked out of my dorm 😂
	It was awesome dude
	But tbh I can’t wait to get back to Maine too
""", """
	Hah dude that sounds like fun, UNE just kicked everybody out on Friday but lol that’s not my problem, and yeah buddy Maine is awesome, gotta love it here
""", """
	Yeah your good lmao. We should hangout sometime when I get back bro
""", """
	I’m down but it’ll prolly have to be a little later, my parents have been skeezing cuz of this virus and since they’re older
""", """
	Oh yeah that totally makes sense I understand bro. But lmk whenever you want to I’m down
""", """
	Word sounds good, hopefully this will die down soon and we’ll be good to chill asap
""", """
	Yeah fr
""", """
	Have fun and stay safe tho, don’t get yourself sick!
""", """
	Aye yeah you too boss
""", """
	👌🏻👌🏻
    """]


trainer = ListTrainer(trainer_bot)

trainer.train(conversation_1)








