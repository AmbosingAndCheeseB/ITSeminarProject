#!/usr/bin/python3

import requests
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, data):
        self.fed.append(data)
        
    def get_data(self):
        return ''.join(self.fed)


def no_tags(html):
    parser = MyParser()
    parser.feed(html)
    return parser.get_data()


url = "https://www.pangdeals.com"

response = requests.get(url)

info = no_tags(response.text)
print(info)
