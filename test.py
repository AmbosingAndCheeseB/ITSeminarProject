from datetime import date
from datetime import timedelta
import re

date1 = []
time = ['1시간전', '2시간전', '3일전', '4일전', '1개월전', '2개월전']

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
print(date1)
