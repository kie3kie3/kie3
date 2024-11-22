import config
import telebot


bot = telebot.TeleBot(config.bot)


def pingLate(penalty, case, name):
    for id in config.admins:
        bot.send_message(id, f"Чел по имени {name} - опоздал. Теперь должен {penalty} денях. Опоздал c этим: {case}")


def writePenalty(db, penalty, case, id, time):
    db[id]['all_penalty'].append([time, penalty, case])
    if id not in db['week_late']:
        db['week_late'][id] = 0
    db['week_late'][id] += penalty
    return db


def moneyCount(time, shedule):
    delta = (time - shedule) // 60
    for i in config.prices:
        if i[0] > delta:
            return i[1]
    return config.max_price


def checkLate(db, time, case, id):
    shedule = db['checker']['shedule'][case]
    if time > shedule:
        penalty = moneyCount(time, shedule)
        db = writePenalty(db, penalty, case, id, time)
        pingLate(penalty, case, db[id]['name'])
    return db