#!/usr/bin/python3

import requests

url = "https://www.pangdeals.com"
response = requests.get(url)
text = response.text
print(text)
