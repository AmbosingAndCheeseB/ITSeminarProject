#!/usr/bin/python3

import requests
from html.parser import HTMLParser


class InfoParser(HTMLParser):

    parser_data = []

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

#    def handle_starttag(self, tag, attrs):

#    def handle_data(self, data):

    def close(self):
        HTMLParser.close(self)


class linkParser(HTMLParser):

    parser_link = []

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

#    def handle_starttag(self, tag, attrs):

    def close(self):
        HTMLParser.close(self)


def info_crawler(text):
    parser = InfoParser()
    parser.feed(text)
    data = parser.parser_data
    return data


def link_crawler(text):
    parser = linkParser()
    parser.feed(text)
    data = parser.parser_link
    return data


url = "http://www.ajpeople.com/bbs/board.php?bo_table=hotdeal#"
response = requests.get(url)

info = info_crawler(response.text)
link = link_crawler(response.text)
print(info)
print(link)
