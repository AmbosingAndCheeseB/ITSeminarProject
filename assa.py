#!/usr/bin/python3

import requests
from html.parser import HTMLParser


class InfoParser(HTMLParser):

    this_tag = ''
    last_tag = ''
    crawling_ok = False
    level_ok = True
    parser_data = []

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            for name, value in attrs:
                if name == 'class' and 'bo_best' not in value and 'bo_notice' not in value:
                    self.crawling_ok = True

        self.this_tag = tag

    def handle_data(self, data):
        if self.this_tag == 'span' and data == 'Lv2.':
            self.level_ok = False

        if self.crawling_ok and self.level_ok:
            if self.this_tag == 'font' and self.last_tag == 'a':
                if '[종료]' not in data:
                    self.parser_data.append(data)

        if self.this_tag == 'font' and self.last_tag == 'a':
            self.level_ok = True

        self.last_tag = self.this_tag

    def handle_endtag(self, tag):
        if tag == 'tbody':
            self.crawling_ok = False

    def close(self):
        HTMLParser.close(self)


class linkParser(HTMLParser):

    crawling_ok = False
    last_value = ''
    parser_link = []

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            for name, value in attrs:
                if name == 'class' and value == '':
                    self.crawling_ok = True

        if tag == "a" and self.crawling_ok:
            for name, value in attrs:
                if name == "href" and self.last_value == 'td_subject':
                    if value is not '#':
                        self.parser_link.append(value)

        for name, value in attrs:
            self.last_value = value

    def handle_data(self, data):
        if '[종료]' in data:
            self.parser_link.pop()

    def handle_endtag(self, tag):
        if tag == 'tbody':
            self.crawling_ok = False

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


for i in range(1, 10):
    url = "http://www.ajpeople.com/bbs/board.php?bo_table=hotdeal&page="+str(i)
    response = requests.get(url)
    info = info_crawler(response.text)
    link = link_crawler(response.text)

print(info)
print(link)