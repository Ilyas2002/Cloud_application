#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import telebot
import time
import schedule

TOKEN = '1475103112:AAGa7bd9Gn7towMFPISaPDnToYBMDz2trJI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')

def weather():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko)'}
    resp = requests.get('https://www.stoloto.ru/top3/archive', headers=headers).text
    soup = BeautifulSoup(resp, "html.parser")
    title = soup.find_all(class_='container cleared')
    resp1 = requests.get('https://www.lotonews.ru/archive/top3', headers=headers).text
    soup1 = BeautifulSoup(resp1, "html.parser")
    title0 = soup1.find('div', class_='table-archive__cell_tirag').text
    resp2 = requests.get('https://www.stoloto.ru/top3/archive', headers=headers).text
    soup2 = BeautifulSoup(resp2, "html.parser")


#ЧИСЛА ТИРАЖА
    title1 = (title[0]).text
    title2 = (title[1]).text
    title3 = (title[2]).text
    title4 = (title[3]).text
    title5 = (title[4]).text
    title6 = (title[5]).text
    title7 = (title[6]).text
    title8 = (title[7]).text
    title9 = (title[8]).text
    title10 = (title[9]).text
#ТОЖЕ ЧИСЛА ТИРАЖА
    title100 = (', '.join(title1.split()))
    title200 = (', '.join(title2.split()))
    title300 = (', '.join(title3.split()))
    title400 = (', '.join(title4.split()))
    title500 = (', '.join(title5.split()))
    title600 = (', '.join(title6.split()))
    title700 = (', '.join(title7.split()))
    title800 = (', '.join(title8.split()))
    title900 = (', '.join(title9.split()))
    title1000 = (', '.join(title10.split()))
#НУМЕРАЦИЯ ТИРАЖА
    title5000 = (int(title0) + 1)
#РАЗДЕЛЕНИЕ ЧИСЕЛ НА ИНДЕКСЫ
    title10100 = (title100[0])
    title10200 = (title100[3])
    title10300 = (title100[6])
    title10400 = (title200[0])
    title10500 = (title200[3])
    title10600 = (title200[6])
    title10700 = (title300[0])
    title10800 = (title300[3])
    title10900 = (title300[6])
    title11000 = (title400[0])
    title11100 = (title400[3])
    title11200 = (title400[6])
    title11300 = (title500[0])
    title11400 = (title500[3])
    title11500 = (title500[6])
    title11600 = (title600[0])
    title11700 = (title600[3])
    title11800 = (title600[6])
    title11900 = (title700[0])
    title12000 = (title700[3])
    title12100 = (title700[6])
    title12200 = (title800[0])
    title12300 = (title800[3])
    title12400 = (title800[6])
    title12500 = (title900[0])
    title12600 = (title900[3])
    title12700 = (title900[6])
    title12800 = (title1000[0])
    title12900 = (title1000[3])
    title13000 = (title1000[6])

    x0 = int(0)
    x1 = int(1)
    x2 = int(2)
    x3 = int(3)
    x4 = int(4)
    x5 = int(5)
    x6 = int(6)
    x7 = int(7)
    x8 = int(8)
    x9 = int(9)


    spisokfa = [title10100, title10200, title10300, title10400, title10500, title10600, title10700, title10800, title10900, title11000, title11100, title11200, title11300, title11400, title11500, title11600, title11700, title11800, title11900, title12000, title12100, title12200, title12300, title12400, title12500, title12600, title12700, title12800, title12900, title13000]

    for i in spisokfa:
        if int(i) == int(0):
            x0 = str('.')
        elif int(i) == int(1):
            x1 = str('.')
        elif int(i) == int(2):
            x2 = str('.')
        elif int(i) == int(3):
            x3 = str('.')
        elif int(i) == int(4):
            x4 = str('.')
        elif int(i) == int(5):
            x5 = str('.')
        elif int(i) == int(6):
            x6 = str('.')
        elif int(i) == int(7):
            x7 = str('.')
        elif int(i) == int(8):
            x8 = str('.')
        elif int(i) == int(9):
            x9 = str('.')



    if x0 == 0:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 0')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)
    if x1 == 1:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 1')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)
    if x2 == 2:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 2')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)
    if x3 == 3:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 3')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)
    if x4 == 4:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 4')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)
    if x5 == 5:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 5')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)
    if x6 == 6:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 6')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)
    if x7 == 7:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 7')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)
    if x8 == 8:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 8')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)
    if x9 == 9:
        bot.send_message(-1001446072664, 'Прогонз:' + '\n' + 'В тираже ' + str(title5000) + '\n' + 'Ставь на: 9')
        time.sleep(300)
        time.sleep(300)
        time.sleep(300)
        time.sleep(120)


schedule.every(1).minutes.do(weather)

while True:
    schedule.run_pending()
    time.sleep(5)

