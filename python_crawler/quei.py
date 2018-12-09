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
        self.is_subject = False
        self.crawling_ok = False

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag

        if tag == 'li':
            for name, value in attrs:
                if name == 'class' and 'bg-black' not in value:
                    self.crawling_ok = True
        else:
            for name, value in attrs:
                self.last_attrs = value

    def handle_data(self, data):
        if self.lasttag == 'div' and self.last_attrs == 'wr-date fs11 hidden-xs' and self.crawling_ok:
            self.parser_date.append(data)

    def handle_endtag(self, tag):
        if tag == 'li':
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

#text parser
class textParser(HTMLParser):

    last_tag = ''
    last_attrs = ''
    parser_text = []
    temp_str = ''

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.crawling_ok = False
        self.is_notice = True

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        if tag == 'li':
            for name, value in attrs:
                if name == 'class' and 'bg-black' not in value:
                    self.is_notice = False

        for name, value in attrs:
            self.last_attrs = value
            if value == 'description' and not self.is_notice:
                self.crawling_ok = True

    def handle_data(self, data):

        if  self.crawling_ok:
            self.temp_str = self.temp_str + data
            self.temp_str = self.temp_str.strip()
            self.temp_str = self.temp_str + " "


    def handle_endtag(self, tag):
        if tag == 'div':
            self.parser_text.append(self.temp_str)
            self.temp_str = ''
            self.crawling_ok = False
            self.is_notice = False

    def close(self):
        HTMLParser.close(self)

pass
def text_crawler(s, text):
    s.feed(text)
    text1 = ''

    for item in s.parser_text:
        temp = str(item.strip())
        if temp:
            text1 = temp


    return text1
pass


connect = pymysql.connect(host = 'localhost',port = 3306, user = 'root', password = 'Tjdduswldnjs12', db = 'ITProj', charset='utf8')

curs = connect.cursor()

sql1 = """Truncate table quei_board"""

curs.execute(sql1)

connect.commit()

index = 0
for i in range(1, 6):
    url = "https://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo&sca=%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4&page="+str(i)

    html_result = requests.get(url)

    link_parser = OurParser()
    subject_parser = subjectParser()
    date_parser = dateParser()

    only_href(link_parser, html_result.text)

    link = need_href(link_parser)
    subject = subject_crawler(subject_parser, html_result.text)
    date1 = date_crawler(date_parser, html_result.text)

    for j in range(0, 30):
        url = link[j]

        html_result = requests.get(url)

        text = textParser()
        text_parser = text_crawler(text, html_result.text)

        if (index == 269):
            break
        real_text = ''
        for k in text_parser:
            real_text = real_text + k

        if '종료' not in subject[index] and '품절' not in subject[index] and '중복' not in subject[index] and '펑' not in subject[index]:
            sql1 = """insert into quei_board(board_num, q_title, q_link, q_date, q_text) 
                             values(null,%s, %s, %s, %s)"""

            curs.execute(sql1, (str(subject[index]), str(link[j]), str(date1[index]), real_text))

        index = 1 + index

connect.commit()

connect.close()