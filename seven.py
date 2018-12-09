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

        if tag == 'tr':
            for name, value in attrs:
                if name== 'class' and 'bo_notice' not in value:
                    self.crawling_ok = True

        if tag == "a":
            for name, value in attrs:
                if name == "href" and self.crawling_ok:
                    self.link.append(value)

    def handle_endtag(self, tag):
        if tag == 'tr':
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
        if 'coupon' in item and 'wr_id' in item and 'page' in item:
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
        if tag == 'tr':
            for name, value in attrs:
                if name== 'class' and 'bo_notice' not in value:
                    self.crawling_ok = True

        for name, value in attrs:
            if value == 'bo_tit' and self.crawling_ok:
                self.is_subject = True

    def handle_data(self, data):

        if self.is_subject and self.last_tag == 'a':
            self.parser_sub.append(data)
        if self.last_tag == 'a':
            self.is_subject = False

    def handle_endtag(self, tag):
        if tag == 'tr':
            self.crawling_ok = False

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


#date parser
class dateParser(HTMLParser):

    last_tag = ''
    last_attrs = ''
    parser_date = []

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.crawling_ok = False

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        if tag == 'tr':
            for name, value in attrs:
                if name == 'class' and 'bo_notice' not in value:
                    self.crawling_ok = True

        for name, value in attrs:
            self.last_attrs = value

    def handle_data(self, data):

        if self.last_tag == 'td' and self.last_attrs == 'td_date' and self.crawling_ok:
            self.parser_date.append(data)


    def handle_endtag(self, tag):
        if tag == 'tr':
            self.crawling_ok = False

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

sql1 = """Truncate table seven_board"""

curs.execute(sql1)

connect.commit()


index = 0
stop = 0
for i in range(0, 10):
    url = "https://www.sevenzone.com/bbs/board.php?bo_table=coupon&page=" + str(i)

    html_result = requests.get(url)
    link_parser = OurParser()
    sub_parser = subjectParser()
    date_parser = dateParser()

    only_href(link_parser, html_result.text)

    subject = subject_crawler(sub_parser, html_result.text)
    date_list = date_crawler(date_parser, html_result.text)
    link = need_href(link_parser)

    stop = len(subject) + stop
    for j in range(0, len(link)):

        if (index == stop):
            break

        if '종료' not in subject[index] or '품절' not in subject[index] or '중복' not in subject[index] or '펑' not in subject[index]:
            sql1 = """insert into seven_board(board_num, s_title, s_link, s_date) 
                                 values(null,%s, %s, %s)"""

            curs.execute(sql1, (str(subject[index]), str(link[j]), str(date_list[index])))

        index = 1 + index

connect.commit()

connect.close()

