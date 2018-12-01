#!/usr/bin/python3

import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print("start tag: ",tag)

    def handle_endtag(self,tag):
        print("end tag: ",tag)

    def handle_data(self,data):
        print("data: ",data)

parser = MyHTMLParser()
parser.feed('<html><head><title>test</title></head></html>')

#url = "https://www.pangdeals.com"
#response = requests.get(url)

#parser=MyHTMLParser()
#parser.feed(response.text)
