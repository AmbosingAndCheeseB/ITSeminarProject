#!/usr/bin/python3

import requests
from html.parser import HTMLParser


class InfoParser(HTMLParser):

    last_tag = ''
    parser_data = ''

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag

    def handle_data(self, data):
        if self.last_tag == 'span':
            self.parser_data += data

    def close(self):
        HTMLParser.close(self)


def info_crawler(text):
    parser = InfoParser()
    parser.feed(text)
    return parser.parser_data


url = "https://www.pangdeals.com"
response = requests.get(url)

info = info_crawler(response.text)
print(info)
