bot = ''
admins = [
    1111687369,
    359510063
]
text = 'Шли фотку'
wait_list = ['Утро кал', 'Утро бар', "Вентиляха", "Хоста", "Табачки", "Вечер"]
hostes = False
time_late = {
    'Утро кал' : [10, 45],
    'Утро бар' : [10, 45],
    "Вентиляха": [11, 5],
    "Хоста" : [12, 0],
    "Табачки" : [17, 0],
    "Вечер" : [16, 50]
}
wday = ['Утро кал', 'Утро бар', "Вентиляха", "Хоста"]
last = 'Табачки'
prices = [
    [10, 200],
    [20, 400],
    [30, 800],
    [60, 1000]
]
max_price = 1500
URL = "https://api.telegram.org/bot" + bot