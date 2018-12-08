#!/usr/bin/python3

import requests
from html.parser import HTMLParser


# link parser

class OurParser(HTMLParser):
    last_tag = ''

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.link = []
        self.crawling_ok = False

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        if tag == 'tr':
            for name, value in attrs:
                if name == 'class' and 'bo_best' not in value and 'bo_notice' not in value:
                    self.crawling_ok = True

        if tag == "a":
            for name, value in attrs:
                if name == "href" and self.crawling_ok:
                    self.link.append(value)

    def handle_data(self, data):
        if self.last_tag == 'span' and 'Lv2' in data:
            self.link.pop()

    def handle_endtag(self, tag):
        if tag == 'a':
            self.crawling_ok = False

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
        if 'hotdeal&' in item and 'wr_id' in item and 'page=' in item:
            new_link.append(item)
    real_link = []

    # boare num = 30
    i = 1
    for item in new_link:
        if i <= 30:
            real_link.append(item)
        i = i + 1
    return real_link


# subject parser
class subjectParser(HTMLParser):
    last_tag = ''
    last_attrs = ''
    parser_sub = []

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.is_subject = False
        self.crawling_ok = False
        self.level_ok = False

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        if tag == 'tr':
            for name, value in attrs:
                if name == 'class' and 'bo_best' not in value and 'bo_notice' not in value:
                    self.crawling_ok = True

        for name, value in attrs:
            self.last_attrs = value
            if value == 'td_subject' and self.crawling_ok:
                self.is_subject = True

    def handle_data(self, data):

        if 'Lv2' in data:
            self.level_ok = False

        if self.is_subject and self.last_tag == 'font' and self.level_ok:
            self.parser_sub.append(data)

    def handle_endtag(self, tag):
        self.last_tag = tag
        if tag == 'tr':
            self.crawling_ok = False
        if self.last_tag == 'font':
            self.is_subject = False
            self.level_ok = True

    def close(self):
        HTMLParser.close(self)


pass


def subject_crawler(s, text):
    s.feed(text)
    subject = []
    print(s.parser_sub)
    print(len(s.parser_sub))
    for item in s.parser_sub:
        temp = str(item.strip())
        if temp:
            subject.append(temp)
    return subject


pass


# date parser
class dateParser(HTMLParser):
    last_tag = ''
    last_attrs = ''
    parser_date = []

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.is_date = False
        self.crawling_ok = False
        self.level_ok = False

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        if tag == 'tr':
            for name, value in attrs:
                if name == 'class' and 'bo_best' not in value and 'bo_notice' not in value:
                    self.crawling_ok = True

        for name, value in attrs:
            self.last_attrs = value
            if value == 'td_date' and self.crawling_ok:
                self.is_date = True

    def handle_data(self, data):

        if 'Lv2' in data:
            self.level_ok = False

        if self.last_tag == 'td' and self.is_date and self.level_ok:
            self.parser_date.append(data)

    def handle_endtag(self, tag):
        if tag == 'tr':
            self.crawling_ok = False
            self.level_ok = True
            self.is_date = False

    def close(self):
        HTMLParser.close(self)


pass


def date_crawler(d, text):
    d.feed(text)
    date = []

    for item in d.parser_date:
        temp = str(item.strip())
        if temp:
            date.append(temp)

    return date


pass

for i in range(0, 10):
    url = "http://www.ajpeople.com/bbs/board.php?bo_table=hotdeal&page=" + str(i)
    response = requests.get(url)

    link = OurParser()
    subject = subjectParser()
    date = dateParser()

    only_href(link, response.text)

    subject_parser = subject_crawler(subject, response.text)
    date_parser = date_crawler(date, response.text)
    link_parser = need_href(link)

