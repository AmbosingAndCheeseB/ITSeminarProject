#!/usr/bin/python3

import requests
from html.parser import HTMLParser

class MyParser(HTMLParser):

    def handle_data(self, data):
        print("some data:",data)


url = "https://www.pangdeals.com"
response = requests.get(url)

parser = MyParser()
parser.feed(response.text)
