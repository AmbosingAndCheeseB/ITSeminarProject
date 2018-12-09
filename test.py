
import requests
from html.parser import HTMLParser

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

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        for name, value in attrs:
            self.last_attrs = value
            if value == 'bo_v_con':
                self.crawling_ok = True

    def handle_data(self, data):

        if  self.crawling_ok and self.last_tag == 'p':
            self.temp_str = self.temp_str + data
            self.temp_str = self.temp_str.strip()
            self.temp_str = self.temp_str + " "


    def handle_endtag(self, tag):
        if tag == 'div':
            self.parser_text.append(self.temp_str)
            self.temp_str = ''
            self.crawling_ok = False

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

for i in range(0, 10):
    url = "http://www.coolenjoy.net/bbs/jirum/1174197?sca=PC%EA%B4%80%EB%A0%A8"
    html_result = requests.get(url)
    text = textParser()
    text_parser = text_crawler(text, html_result.text)


print(text_parser)