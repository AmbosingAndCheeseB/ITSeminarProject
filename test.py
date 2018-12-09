import os

result = os.popen('wget http://www.ajpeople.com/bbs/board.php?bo_table=hotdeal&page=1')
f = open("./board.php?bo_table=hotdeal", 'r')
data = f.read()
print(data)