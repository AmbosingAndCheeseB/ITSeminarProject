#!/usr/bin/python3

import requests
from html.parser import HTMLParser


class MyParser(HTMLParser):

    def __init__(self):
        self.reset()
        self.fed = []

#    def handle_starttag(self, tag, attrs):
#        print("start tag: ", tag)

#    def handle_endtag(self, tag):
#        print("end tag: ", tag)

    def handle_data(self, data):
        self.fed.append(data)

    def get_data(self):
        return ''.join(self.fed)


def only_info(html):
    parser = MyParser()
    parser.feed(html)
    return parser.get_data()


url = "https://www.pangdeals.com"

response = requests.get(url)

info = only_info(response.text)
print(info)
