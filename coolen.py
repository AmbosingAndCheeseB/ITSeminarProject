#!/usr/bin/python3

import requests
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



url = "http://www.coolenjoy.net/bbs/jirum/p1"

html_result = requests.get(url)

print(strip_tags(html_result.text))
