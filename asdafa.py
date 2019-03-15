import telebot
from telebot import types
bot = telebot.TeleBot("707805764:AAFU5h5CTbZvzmdkWheQi2p0U8H79sGZACs")
sum_dict=[]
@bot.message_handler(commands=['start'])

def start(message):
    sent = bot.send_message(message.chat.id, "Enter mass")
    bot.register_next_step_handler(sent,hello)

def hello(message):
    bot.send_message(message.chat.id, "your entered mass is {mass}".format(mass=message.text))
    sent1 = bot.send_message(message.chat.id, "Enter acceleration")
    bot.register_next_step_handler(sent1, hello1)

def hello1(message):
    bot.send_message(message.chat.id, "your entered acceleration is {acceleration}".format(acceleration=message.text))


bot.polling()