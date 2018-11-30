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
        print("data:",data)


url = "https://www.pangdeals.com"
response = requests.get(url)

parser = MyParser()
parser.feed(response.text)
