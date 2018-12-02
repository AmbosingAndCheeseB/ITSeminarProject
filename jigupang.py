#!/usr/bin/python3

import requests
from html.parser import HTMLParser


class MyParser(HTMLParser):

    last_tag = ''
    text = ''

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag

    def handle_data(self, data):
        if self.last_tag == 'span':
            self.text += data
            return self.text

    def close(self):
        HTMLParser.close(self)


parser = MyParser()

url = "https://www.pangdeals.com"
response = requests.get(url)

parser.feed(response.text)
print(parser.text)
