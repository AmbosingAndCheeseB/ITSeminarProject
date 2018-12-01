#!/usr/bin/python3

import requests
from html.parser import HTMLParser


class MyParser(HTMLParser):

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_starttag(self, tag, attrs):
        self.fed.append('<')
        self.fed.append(tag)
        self.fed.append('>')

    def handle_endtag(self, tag):
        self.fed.append('</')
        self.fed.append(tag)
        self.fed.append('>')

    def handle_data(self, data):
        self.fed.append(data)

    def get_data(self):
        return ''.join(self.fed)


parser = MyParser()

url = "https://www.pangdeals.com"
response = requests.get(url)

parser.feed(response.text)

text = parser.get_data()
print(text)
