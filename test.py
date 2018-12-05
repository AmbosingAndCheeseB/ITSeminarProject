import pymysql

conn = pymysql.connect(host='localhost', user='root', password='Tjdduswldnjs12',
                       db='ITProj', charset='utf8')

curs = conn.cursor()
sql = """insert into coolen_board(board_id, c_title, c_link, c_date)
         values (null, %s, %s, %s)"""
print(sql)
curs.execute(sql, ('홍길동', 1, '서울'))
curs.execute(sql, ('이연수', 2, '서울'))
conn.commit()

conn.close()