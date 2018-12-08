#!/usr/bin/python3

import requests
from html.parser import HTMLParser
from selenium import webdriver
import time


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




url = "https://www.pangdeals.com"

chromedriver_dir = 'C:\Users\yang\Desktop\chromedriver_win32'
driver = webdriver.Chrome(chromedriver_dir)
time.sleep(5)

loca = driver.find_element_by_class_name('box')
loca.click()
time.sleep(5)

response = requests.get(url)

driver.get(url)

info = info_crawler(response.text)
time = time_crawler(response.text)
link = link_crawler(response.text)

print(info)
print(time)
print(link)

count = 0
for i in info:
    count += 1

print(count)

count = 0
for j in time:
    count += 1

print(count)

count = 0
for k in link:
    count += 1

print(count)