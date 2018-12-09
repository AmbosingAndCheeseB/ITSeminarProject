
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
        self.is_text = False

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        for name, value in attrs:
            if value == 'desc':
                self.is_text = True

    def handle_data(self, data):

        if self.is_text:
            self.temp_str = self.temp_str + data
            self.temp_str = self.temp_str.strip()
            self.temp_str = self.temp_str + " "

    def handle_endtag(self, tag):

        if tag == 'p':
            self.parser_text.append(self.temp_str)
            self.temp_str = ''
            self.is_text = False

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



url = "https://www.pangdeals.com/hotdeals/detail/32250"
html_result = requests.get(url)
text = textParser()
text_parser = text_crawler(text, html_result.text)
test = ''
for k in text_parser:
    test = test + k

print(test)