from datetime import date
from datetime import timedelta
import time

date1 = ['12-08', '12-07']
now = time.localtime()
print(now.tm_year)

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