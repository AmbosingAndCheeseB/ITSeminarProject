#!/usr/bin/python3

import requests
from html.parser import HTMLParser

class OurParser(HTMLParser):

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.link = []

    def handle_starttag(self, tag, attrs):
                if tag == "a":
                    for name, value in attrs:
                        if name == "href":
                            self.link.append(value)
    def get_link(self):
        return self.link

pass


def only_href(s, html):
    s.feed(html)
    try:

        s.handle_starttag()
    except:
        return

def need_href(s):
    temp = s.get_link()
    new_link = []
    for item in temp:
        if '/jirum/' in item and '?sca=PC' in item:
            new_link.append(item)
    return new_link


url = "http://www.coolenjoy.net/bbs/jirum?sca=PC%EA%B4%80%EB%A0%A8"

html_result = requests.get(url)
s = OurParser()

only_href(s, html_result.text)

print(s.get_link())

print(need_href(s))