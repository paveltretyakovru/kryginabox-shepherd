#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

from datetime import datetime as dt

filename = 'data'

def loadData():
    today = dt.today()
    today = dt.strftime(today, "%Y.%m.%d")

    if os.stat(filename).st_size:
        with open(filename) as data_file:
            data = json.load(data_file)

            # Обнуляем счетчик
            if not data['today'] == today:
                data['countToday'] = 0
                data['today'] = today
                data['controllMessage'] = True
    else:
        data = dict(last = '', count = 0, countToday = 0, today = today)

    return data
