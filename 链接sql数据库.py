import pymysql
# 1. 建立链接对象
conn = pymysql.Connect(host='127.0.0.1',user = 'root',
                       password ='4866098',db = 'homework_student',
                       port = 3306,charset = 'utf8')

# conn1 = pymysql.Connect(host='127.0.0.1',user = 'root',
#                        password ='4866098',db = 'bzx',
#                        port = 3306,charset = 'utf8')

# print(conn,type(conn))
# 2.创建游标对象
cursor = conn.cursor()

# 3.执行sql语句
sql = "create table if not exists test (name varchar(200), id int primary key )"
cursor.execute(sql)
cursor.close()
conn.close()