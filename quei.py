#!/usr/bin/python3

import requests
from html.parser import HTMLParser
import re
import pymysql
from datetime import date


#link parser
class OurParser(HTMLParser):

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.link = []
        self.crawling_ok = False

    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            for name, value in attrs:
                if name == 'class' and 'bg-black' not in value:
                    self.crawling_ok = True

        if tag == "a":
            for name, value in attrs:
                if name == "href" and self.crawling_ok:
                    self.link.append(value)

    def handle_endtag(self, tag):
        if tag == 'li':
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
        if 'qb_saleinfo&' in item and 'wr_id' in item:
            new_link.append(item)
    real_link = []

    # boare num = 25
    i = 1
    for item in new_link:
        if i <= 25:
            real_link.append(item)
        i = i+1
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


    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        if tag == 'li':
            for name, value in attrs:
                if name == 'class' and 'bg-black' not in value:
                    self.crawling_ok = True

        for name, value in attrs:
            self.last_attrs = value
            if value == 'item-subject' and self.crawling_ok:
                self.is_subject = True

    def handle_data(self, data):

        if self.is_subject and self.last_tag == 'a' and self.this_tag == 'span':
            self.parser_sub.append(data)

        if self.last_tag == 'a' and this_tag == 'span':
            self.is_subject = False




    def handle_endtag(self, tag):
        if tag == 'li':
            self.crawling_ok = False

    def close(self):
        HTMLParser.close(self)

pass


def subject_crawler(s, text):
    s.feed(text)
    subject = []


    for item in s.parser_sub:
        subject.append(re.findall('.+', item))



    return subject
pass


url = "https://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo&sca=%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4&page=1"

html_result = requests.get(url)

link_parser = OurParser()
subject_parser = subjectParser()

only_href(link_parser, html_result.text)

link = need_href(link_parser)
subject = subject_crawler(subject_parser, html_result.text)

print(link)
print(subject)