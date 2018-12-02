#!/usr/bin/python3

import requests
from html.parser import HTMLParser


class InfoParser(HTMLParser):

    last_tag = ''
    last_attrs = ''
    is_end = False
    parser_data = ''

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        for name, value in attrs:
            self.last_attrs = value

    def handle_data(self, data):
        if self.last_attrs == 'mask end':
            self.is_end = True

        if not self.is_end and self.last_tag == 'span' and self.last_attrs == 'txt':
            self.parser_data += data

        if self.last_attrs != 'mask end':
            self.is_end = False

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
