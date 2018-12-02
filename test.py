from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<td class="td_subject"> <a href="http://www.coolenjoy.net/bbs/jirum/1164212?sca=PC%EA%B4%80%EB%A0%A8">[쿠팡] Windows 10 Home FPP 134,850원 / 무배                                    </a> </td>')