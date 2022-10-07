#!/usr/bin/env python

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = '27a5240604149112c63321f31338ec3b080b638c'
API_URL = 'https://api.esv.org/v3/passage/text/'
# https://api.esv.org/docs/passage-text/

class Bible:
    def __init__(self):
        self.p = ""

    def get_esv_text(self, passage):
        params = {
            'q': passage,
            'include-headings': True,
            'include-footnotes': False,
            'include-verse-numbers': True,
            'include-short-copyright': False,
            'include-passage-references': True
        }

        headers = {
            'Authorization': 'Token %s' % API_KEY
        }

        response = requests.get(API_URL, params=params, headers=headers)

        passages = response.json()['passages']

        return passages[0].strip() if passages else 'Error: Passage not found'


if __name__ == '__main__':
    passage = "john 1:1"
    t = Bible()

    if passage:
        print(t.get_esv_text(passage))