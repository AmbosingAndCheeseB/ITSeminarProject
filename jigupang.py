#!/usr/bin/python3

import requests
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_starttag(self,tag,attr):
        if tag == 'span':
            return 1

    def handle_data(self, data):
        if self.handle_data():
            self.fed.append(data)
        
    def get_data(self):
        return ''.join(self.fed)


def only_data(html):
    parser = MyParser()
    parser.feed(html)
    return parser.get_data()


url = "https://www.pangdeals.com"

response = requests.get(url)

info = only_data(response.text)
print(info)
