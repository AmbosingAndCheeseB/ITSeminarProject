#!/usr/bin/python3

import requests
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

#    def handle_starttag(self, tag, attr):


    def handle_data(self, d):
        self.fed.append(d)
        
    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    parser = MyParser()
    parser.feed(html)
    return parser.get_data()

url = "https://www.pangdeals.com"

response = requests.get(url)

print(strip_tags(response.text))
