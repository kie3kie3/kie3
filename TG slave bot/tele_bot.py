import config
import telebot
from telebot import types
import time
from getter import get_info, update
from register import register
from lateMaster import checkLate


bot = telebot.TeleBot(config.bot)


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, "Как звать, тебя человек?")
    bot.register_next_step_handler(msg, register)


def inside(situation, id, db, date):
    print(321)
    db['day_late'][situation] = [True, date, db[id]['name']]
    db[id]['wait'][situation] = False
    return db


def cancel(message):
    db = get_info()
    for i in config.wait_list:
        if db[message.chat.id]['wait'][i]:
            db[message.chat.id]['wait'][i] = False


def photo(message):
    if not message.photo:
        for i in config.wait_list:
            if message.text == i:
                msg = bot.send_message(message.chat.id, 'Я не умею ждать более одной фотки, пиши Отмена, либо шли фотку')
                bot.register_next_step_handler(msg, photo(msg))
                return 0
        if message.text == "Отмена":
            bot.send_message(message.chat.id, 'Отмена, так отмена')
            cancel(message)
            return 1
        else:
            msg = bot.send_message(message.chat.id, 'Сейчас не понял, либо фотку, либо пиши Отмена')
            bot.register_next_step_handler(msg, photo(msg))
            return 2
    for i in config.admins:
        bot.send_photo(i, message.photo[0].file_id)
    db = get_info()
    for i in config.wait_list:
        if db[str(message.chat.id)]['wait'][i]:
            print(123)
            db = inside(i, str(message.chat.id), db, message.date)
            db = checkLate(db, float(message.date), i, str(message.chat.id))
    update(db)


@bot.message_handler()
def markup_txt(message):
    if message.text in config.wait_list:
        db = get_info()
        db[str(message.chat.id)]['wait'][message.text] = True
        update(db)
        msg = bot.send_message(message.chat.id, config.text)
        bot.register_next_step_handler(msg, photo)
    elif message.text == 'id':
        bot.send_message(message.chat.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, 'Чаво?')


def main():
    time.sleep(6)
    print('Старт')
    bot.infinity_polling()