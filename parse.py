import requests
import config
from datetime import datetime, time


def endweek(day):
    return day + 7 * 24 * 60 * 60

def parse():
    response = requests.post(config.URL, config.PAYLOAD)
    if response.status_code != 200:
        return 'Сервак МТИ чудит'
    data = response.json()
    if not data['success']:
        return 'Парсер сломавси'
    if data == {}:
        return 'Сервак на месте, а занятий не нашлось'
    today = int(datetime.combine(datetime.now(), time.min).timestamp())

    lessons = []
    for day in data['data']:
        starttime = int(day['lessons'][0]['dateTime'])
        if starttime < today or starttime > endweek(today):
            continue
        for lesson in day['lessons']:
            lessons.append(lesson)
            
    if lessons == []:
        return 'Пар нема, отдыхай путник'

    day_shedule = f'{lessons[0]["dateTimeString"]}\n'
    for i in range(len(lessons)):
        day_shedule += f'{str(i)} {lessons[i]["lessonTimeString"]} {lessons[i]['disciplineTitle']} {lessons[i]['teacherName']} {lessons[i]['room']}\n'

    return day_shedule