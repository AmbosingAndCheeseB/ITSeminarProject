#!/usr/bin/python3

import requests
from html.parser import HTMLParser

class OurParser(HTMLParser):
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
    s = OurParser()
    s.feed(html)
    return s.get_data()

def only_href(html):
    s = OurParser()
    s.feed(html)
    s.handle_starttag()




url = "http://www.coolenjoy.net/bbs/jirum/p1"

html_result = requests.get(url)

print(strip_tags(html_result.text))

only_href(html_result.text)
