import telebot
import parse
import config

bot = telebot.TeleBot(config.bot)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Прив!')



@bot.message_handler()
def shedule(message):
    bot.send_message(message.chat.id, parse.parse())



bot.polling(non_stop=True)