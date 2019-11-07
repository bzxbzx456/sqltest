import pymysql
# 1.链接数据库
"""
host: 数据库服务器地址
user: 登录帐号
password:帐号密码
db:指定数据库
port:端口 默认3306
charset:指定连接的字符集
"""
from setting import dbparams
# conn = pymysql.Connect(host='127.0.0.1',user = 'root',
#                        password ='4866098',db = 'homework_student',
#                        port = 3306,charset = 'utf8')

conn = pymysql.connect(**dbparams)
# 2.创建一个游标
cursor = conn.cursor()

try:
    sno = input("请输入你的学号：")
    sname = input("请输入你的姓名：")
    ssex = input("请输入你的性别：")
    sbirthday = input("请输入你的生日：")
    sclass = input("请输入你的班级：")
# 返回值是受影响的行数
# 对于增删改操作，因为pymysql 默认开启事物，
# 所以必须手动commit（）或 否则数据库没有数据
#     sql = "insert into student(sno,sname,ssex,sbirthday,sclass) values ('110','孙五','男','1997-10-08','95033')"
    sql = "insert into student(sno,sname,ssex,sbirthday,sclass) values ('{}','{}','{}','{}','{}')".format(sno,sname,ssex,sbirthday,sclass)
    print(sql)
    result = cursor.execute(sql)
    conn.commit()
    print(result)
    if result>0:
        print("Ture")
    else:
        print("False")
except Exception as e:
    print(e)
    conn.rollback()
finally:
    # 4.关闭游标
    cursor.close()
    conn.close()




