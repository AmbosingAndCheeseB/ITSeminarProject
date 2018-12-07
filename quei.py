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
        if i <= 30:
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
            if value == 'wr-subject' and self.crawling_ok:
                self.is_subject = True

    def handle_data(self, data):

        if self.is_subject and self.last_tag == 'span':
            self.parser_sub.append(data)






    def handle_endtag(self, tag):
        self.last_tag = tag
        if tag == 'li':
            self.crawling_ok = False
        if self.last_tag == 'a':
            self.is_subject = False

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

connect = pymysql.connect(host = 'localhost',port = 3306, user = 'root', password = 'Tjdduswldnjs12', db = 'ITProj', charset='utf8')

curs = connect.cursor()

index = 0
for i in range(1, 10):
    url = "https://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo&sca=%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4&page="+str(i)

    html_result = requests.get(url)

    link_parser = OurParser()
    subject_parser = subjectParser()

    only_href(link_parser, html_result.text)

    link = need_href(link_parser)
    subject = subject_crawler(subject_parser, html_result.text)

    for j in range(0, 30):

        if (index == 270):
            break

        temp = str(subject[index][1])
        if '종료' not in subject[index] or '품절' not in subject[index] or '중복' not in subject[index] or '펑' not in subject[index]:
            sql1 = """insert into quei_board(board_id, c_title, c_link, c_date) 
                             values(null,%s, %s, %s)"""
            print(sql1)
            curs.execute(sql1, (subject[index], str(link[j]), str(date.today())))

        index = 1 + index

    print(link)

    print(subject)
    print(len(link))
    print(len(subject))

connect.commit()
connect.close()