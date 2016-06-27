#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime as dt

filename = 'data'

def writeData(data):

    if isinstance(data, dict):
        writeData = data
    else:
        writeData = {}

    # Инкрементируем счетчики
    writeData['countToday'] = writeData['countToday'] + 1
    writeData['count'] = writeData['count'] + 1
    writeData['time'] = dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S')

    with open(filename, 'w') as outfile:
        json.dump(writeData, outfile)

    return data
