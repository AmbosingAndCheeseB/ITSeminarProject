#!/usr/bin/python3

import requests
from html.parser import HTMLParser
import re
import pymysql
from datetime import date

connect = pymysql.connect(host = '106.10.37.154',port = 3306, user = 'root', password = 'Tjdduswldnjs12', db = 'ITProj', charset='utf8')

curs = connect.cursor()

#link parser
class OurParser(HTMLParser):

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.link = []

    def handle_starttag(self, tag, attrs):
                if tag == "a":
                    for name, value in attrs:
                        if name == "href":
                            self.link.append(value)
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
        if '/jirum/' in item and '?sca=PC' in item:
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

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        for name, value in attrs:
            self.last_attrs = value
            if value == 'td_subject':
                self.is_subject = True

    def handle_data(self, data):

        if self.is_subject and self.last_tag == 'a':
            self.parser_sub.append(data)
        if self.last_tag == 'a':
            self.is_subject = False


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

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        for name, value in attrs:
            self.last_attrs = value


    def handle_data(self, data):

        if self.last_tag == 'td' and self.last_attrs == 'td_date':
            self.parser_date.append(data)



    def close(self):
        HTMLParser.close(self)

pass

def date_crawler(d, text):
    d.feed(text)
    date = []
    for item in d.parser_date:
        date.append(re.findall('.+', item))

    return date
pass




for i in range(1,10):
    url = "http://www.coolenjoy.net/bbs/jirum/p"+str(i)+"?sca=PC%EA%B4%80%EB%A0%A8"

    html_result = requests.get(url)
    link_parser = OurParser()
    sub_parser = subjectParser()
    date_parser = dateParser()

    only_href(link_parser, html_result.text)



    subject = subject_crawler(sub_parser, html_result.text)
    date_list = date_crawler(date_parser, html_result.text)
    link = need_href(link_parser)


    for j in range(0, 25):
        index = j*i
        temp = str(subject[index][1])
        if ":" in date_list[index][0] and temp.replace(" ", ""):
            temp = str(subject[index][1])
            temp = temp.lstrip()
            print(temp.rstrip() + " " + link[j] + " " + str(date.today()))

#    for j in range(0, 25):
 #       index = j*i
  #      if ":" in date.parser_date[index][0] and subject.parser_sub[index][1]:
  #          sql = "insert into coolen_board values(null, " + subject.parser_sub[index][1] + " , " + link[j] + ", " + date.today() + ")"
#
 #           curs.execute(sql)




connect.close()
