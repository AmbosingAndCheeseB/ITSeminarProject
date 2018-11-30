#!/usr/bin/python3

import requests
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    print (name, "=", value)

def strip_tags(html):
    s = MyParser()
    s.feed(html)
    return s.get_data()

def only_href(html):
    s = MyParser()
    s.feed(html)
    s.handle_starttag()




url = "https://www.pangdeals.com"

response = requests.get(url)

print(strip_tags(response.text))

only_href(response.text)

# I add this comment to test git pull
