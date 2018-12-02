#!/usr/bin/python3

import requests
from html.parser import HTMLParser


#link parser
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
    real_link = []

    # boare num = 25
    i = 1
    for item in new_link:
        if i <= 25:
            real_link.append(item)
        i = i+1
    return real_link



# text parser

url = "http://www.coolenjoy.net/bbs/jirum?sca=PC%EA%B4%80%EB%A0%A8"

html_result = requests.get(url)
s = OurParser()

only_href(s, html_result.text)

print(s.get_link())

link = need_href(s)

for item in link:
    print(item)