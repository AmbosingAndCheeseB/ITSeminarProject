#!/usr/bin/python3

import requests
from html.parser import HTMLParser


class InfoParser(HTMLParser):

    last_tag = ''
    last_attrs = ''
    is_end = False
    parser_data = []

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        for name, value in attrs:
            self.last_attrs = value
        if self.last_attrs == 'mask end':
            self.is_end = True

    def handle_data(self, data):
        if not self.is_end and self.last_tag == 'span' and self.last_attrs == 'txt':
            if '\n' not in data:
                temp = data.replace("\xa0", "")
                self.parser_data.append(temp)

        if self.last_tag == 'span' and self.last_attrs == 'txt':
            self.is_end = False

    def close(self):
        HTMLParser.close(self)


class linkParser(HTMLParser):

    parser_link = []
    is_content = False

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value == 'hotdeal_list':
                self.is_content = True

        if tag == "a" and self.is_content:
            for name, value in attrs:
                if name == "href" and 'detail' in value:
                    self.parser_link.append(value)

    def close(self):
        HTMLParser.close(self)


class ImageParser(HTMLParser):

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

#    def handle_starttag(self, tag, attrs):

#    def handle_data(self, data):

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


url = "https://www.pangdeals.com"
response = requests.get(url)

info = info_crawler(response.text)
link = link_crawler(response.text)
print(info)
print(link)
