#!/usr/bin/python3

import requests
from html.parser import HTMLParser


class MyParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("start tag: ", tag)

    def handle_endtag(self, tag):
        print("end tag: ", tag)

    def handle_data(self, data):
        print("data: ", data)


parser = MyParser()

url = "https://www.pangdeals.com"
response = requests.get(url)

parser = MyParser()
parser.feed(response.text)
