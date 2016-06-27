#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import json
from .vkAuth import vkAuth

def sendVkMessage(userid, message):

    # Auth in vk
    selfId, token = vkAuth()

    messText = urllib.parse.urlencode(dict( message = message ))
    messUrl = 'https://api.vk.com/method/messages.send?user_id=%s&%s&access_token=%s&v=5.52' % (userid, messText, token);
    result = json.loads(urllib.request.urlopen(messUrl).read().decode('utf-8'))

    print('Отправлено сообщение', message , '. Результат: ',result)

    return
