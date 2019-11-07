import pymysql
from setting import dbparams
# 1.链接对象
conn = pymysql.Connect(**dbparams)
# 2.创建游标
cursor = conn.cursor()
# 3.执行sql语句
sql = "select sname,sclass from student"
try:
    cursor.execute(sql)
#     4.获取结果集
#     打印所有
#     date = cursor.fetchall()
#     print(date)
#     打印四条
#     date = cursor.fetchmany(4)
#     print(date)
#     打印一条
#     date = cursor.fetchone()
#     print(date)

    # 一条条打印
    date = cursor.fetchone()
    while date:
        print(date)
        date = cursor.fetchone()
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
