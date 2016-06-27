#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import logging
import urllib.request as urllib2
from urllib.error import URLError, HTTPError

from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
from functions.loadData import loadData
from functions.writeData import writeData
from functions.sendVkMessage import sendVkMessage

url = 'http://elenakrygina.com/box/month/puteshestvie-2'
hour = dt.today().hour
containerClass = 'fb-item__name'
randomInt = random.randint(1, 345435435325343)

users = dict( pavel = 217899236, alena = 1322876)

# Work wit data
data = loadData()

# Устанавливаем параметры для логирования
logging.basicConfig(filename='data.log',level=logging.DEBUG)

# Loas site content
try:
    page = urllib2.urlopen(url)
except URLError as e:
    print(e.reason)

    if hour >= 10 and hour < 11 and not data['controllMessage'] == False:
        controllMessage = """
            Привет. Это контрольное робо-письмо сообщает о том, что
            скрипт продалжает слежку за сайтом. За весь рабочий (%s)
            день, страница была сканирована %s раз. За все время,
            она была отсканирована %s раз. (unicid = %s)
            Это расширенное письмо также уведомляет о том, что
            САЙТ С ТОВАРОМ НЕДОСТУПЕН.
        """ % (data['today'], data['countToday'], data['count'], randomInt)

        # Send controll message
        sendVkMessage(users['alena'], controllMessage);
        sendVkMessage(users['pavel'], controllMessage);

    data['error'] = 'Сайт недоступен для чтения'
    data['unicid'] = randomInt
    data['controllMessage'] = False

    logging.debug('%s - сайт недоступен' % dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S'))

else:
    # page = urllib2.urlopen(url)
    page = page.read();

    # Get last box in content container
    last = bs(page).find('div', { 'class' : containerClass }).string

    # Check ident for site value and local file value
    if not last == data['last']:

        # Save new value
        data['last'] = last
        sendVkMessage(users['alena'], 'Урааа!Появлися товар!Скорее покупать! %s %s'%(url, randomInt))
        sendVkMessage(users['pavel'], 'Урааа!Появился товар!Скорее покупать! %s %s'%(url, randomInt))

    else:
        logging.debug('%s - нового товара нет' % dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S'))
        # sendVkMessage(token, userId, 'Нового товара не появилось ;-( %s' % randomInt);

    if hour >= 10 and hour < 11 and not data['controllMessage'] == False:
        controllMessage = """
                          Привет. Это контрольное робо-письмо сообщает о том, что
                          скрипт продалжает слежку за сайтом. За весь рабочий (%s)
                          день, страница была сканирована %s раз. За все время,
                          она была отсканирована %s раз. (unicid = %s)
                          """ % (data['today'], data['countToday'], data['count'], randomInt)

        data['error'] = ''
        data['unicid'] = randomInt
        data['controllMessage'] = False

        # Send controll message
        sendVkMessage(users['alena'], controllMessage);
        sendVkMessage(users['pavel'], controllMessage);

# Записываем новые данные
data = writeData(data)

# Логируем необходимые данные
logging.debug(data)
print('Результат выполнения скрипта:', data)
