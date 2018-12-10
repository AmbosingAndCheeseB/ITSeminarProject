#!/usr/bin/python3

import requests
from html.parser import HTMLParser
import time
import pymysql
import os

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



connect = pymysql.connect(host = 'localhost',port = 3306, user = 'root', password = 'Tjdduswldnjs12', db = 'ITProj', charset='utf8')

curs = connect.cursor()

sql1 = """Truncate table assa_board"""

curs.execute(sql1)

connect.commit()

index = 0
for i in range(1, 10):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    url = "http://www.ajpeople.com/bbs/board.php?bo_table=hotdeal&page=" + str(i)

    response = requests.get(url, headers = headers)
    print(response)
    print(response.text)
    link = OurParser()
    subject = subjectParser()
    date = dateParser()

    only_href(link, response.text)

    subject_parser = subject_crawler(subject, response.text)
    date_parser = date_crawler(date, response.text)
    link_parser = need_href(link)

    print(subject_parser)
    print(link_parser)
    print(len(subject_parser))
    print(len(link_parser))
    date2 = []
    for i in date_parser:
        if ':' in i:
            date2.append(i)
        else:
            now = time.localtime()
            days = str(now.tm_year) + "-" + i
            date2.append(str(days))

    for j in range(0, len(link_parser)):

        if (index == len(subject_parser)-1):
            break

        if '종료' not in subject_parser[index]:
            sql1 = """insert into assa_board(board_num, a_title, a_link, a_date) 
                                    values(null,%s, %s, %s)"""

            curs.execute(sql1, (str(subject_parser[index]), str(link_parser[j]), str(date2[index])))

        index = 1 + index
connect.commit()

connect.close()