#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:14:04 2019

@author: Kshitij Gupta <kshitijgm@gmail.com>
@co-author: Maitreya Patni <maitreyapatni30@gmail.com>
"""

from bs4 import BeautifulSoup
from shutil import which
import requests
import time
import subprocess
import sys

def send_msg(msg):

   bot_token = ''
   bot_chatID = ''
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + msg

   response = requests.get(send_text)

   return response.json()


def main():

    url = 'https://android.googlesource.com/platform/manifest/+refs'
    matching = []

    while len(matching) == 0:
        print('\n[*] Checking!')
        tag_list = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for li in soup.findAll('li', {'class': 'RefList-item'}):
            tag = li.findChildren('a', recursive=False)[0]['href'].split('/')[-1]
            tag_list.append(tag)
        matching = [s for s in tag_list if 'android-12' in s or 'android12' in s]
        if len(matching) > 0:
            test = send_msg("[!] ANDROID 12 IS HERE! @dogbutpink" + '[!] Result: {}'.format(matching))
            print(test)
        else:
            test = send_msg('[*] No Android 12 (yet) 😭')
            print(test)
            time.sleep(20 * 60)  # Wait for 10 minutes
    try:
        from subprocess import DEVNULL
    except ImportError:
        import os
        DEVNULL = open(os.devnull, 'wb')


if __name__ == '__main__':
    main()
