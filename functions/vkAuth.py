#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib
import urllib.request as urllib2
from http.cookiejar import CookieJar
from html.parser import HTMLParser
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
from .authData import authData

from functions.splitKeyValue import splitKeyValue

encoding = 'utf-8'
client_id = 5512115
# scope = 'offline,messages'
scope = 'messages'
email = authData['email']
password = authData['password']
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()),urllib2.HTTPRedirectHandler())

def vkAuth():

    ########################## GET AUTH FROM TIME ##################################
    authUrl = "http://oauth.vk.com/oauth/authorize?" + \
    "redirect_uri=http://oauth.vk.com/blank.html&response_type=token&" + \
    "client_id=%s&scope=%s&display=wap" % (client_id, scope)

    authResponse = opener.open(authUrl)
    authForm = bs(authResponse.read()).find('form')

    ########################## SEND AUTH DATA TIME #################################
    authData = {}
    # Collect form inputs
    for inp in authForm.findAll('input'):
        if not inp['type'] == 'submit':
            authData[inp['name']] = inp.get('value')

    # Insert user parameters
    authData['email'] = email
    authData['pass'] = password
    authData['scope'] = scope
    authData = urllib.parse.urlencode(authData).encode(encoding)

    authResponse = opener.open(authForm['action'], authData)
    authUrl = authResponse.geturl()

    ################### GIVE ACCESS TIME #############################

    # Если появилась страница запроса разрешения прав
    if not urlparse(authUrl).path == "/blank.html":
        accessForm = bs(authResponse.read()).find('form')
        accessUrl = accessForm['action']
        accessResponse = opener.open(accessUrl)
        accessUrl = accessResponse.geturl()
    else:
        accessUrl = authUrl

        accessResult = dict(splitKeyValue(kv_pair) for kv_pair in urlparse(accessUrl).fragment.split('&'))
        userId = accessResult['user_id']
        token = accessResult['access_token']

    return userId, token
