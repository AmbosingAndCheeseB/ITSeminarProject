#!/usr/bin/python3

import requests
from html.parser import HTMLParser
from selenium import webdriver
from datetime import date
from datetime import timedelta
import time
import pymysql
import re



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


class TimeParser(HTMLParser):

    last_tag = ''
    last_attrs = ''
    is_end = False
    parser_time = []

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
        if not self.is_end and self.last_tag == 'span' and self.last_attrs == 'time':
            if '\n' not in data:
                self.parser_time.append(data)

        if self.last_tag == 'span' and self.last_attrs == 'hit':
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
                    data = 'https://www.pangdeals.com' + value
                    self.parser_link.append(data)

        for name, value in attrs:
            if value == 'mask end':
                self.parser_link.pop()

    def close(self):
        HTMLParser.close(self)


def info_crawler(text):
    parser = InfoParser()
    parser.feed(text)
    data = parser.parser_data
    return data


def time_crawler(text):
    parser = TimeParser()
    parser.feed(text)
    data = parser.parser_time
    return data


def link_crawler(text):
    parser = linkParser()
    parser.feed(text)
    data = parser.parser_link
    return data


connect = pymysql.connect(host = 'localhost',port = 3306, user = 'root', password = 'Tjdduswldnjs12', db = 'ITProj', charset='utf8')

curs = connect.cursor()

sql1 = """Truncate table pang_board"""

curs.execute(sql1)

connect.commit()




url = "https://www.pangdeals.com"


driver =webdriver.PhantomJS()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(5)

for i in range(0, 5):
    loca = driver.find_element_by_class_name('box')
    loca.click()
    time.sleep(5)
source = driver.page_source

info = info_crawler(source)
time = time_crawler(source)
link = link_crawler(source)

print(info)
print(time)
print(link)
date1 = []

for i in time:
    if '시간전' in i:
        date1.append(str(date.today()))
    elif '일전' in i:
        today = date.today()
        temp = re.findall('\d+', i)
        temp = int(temp.pop())
        now = timedelta(days=temp)
        days = today - now
        date1.append(str(days))
    elif '개월전' in i:
        today = date.today()
        temp = re.findall('\d+', i)
        temp = int(temp.pop())
        temp = temp * 30
        now = timedelta(days=temp)
        days = today - now
        date1.append(str(days))

for i in range(len(info)):
    sql1 = """insert into pang_board(board_num, p_title, p_link, p_date) 
                              values(null,%s, %s, %s)"""

    curs.execute(sql1, (info[i], link[i], date1[i]))

driver.quit()

connect.commit()
connect.close()