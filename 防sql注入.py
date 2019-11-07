import pymysql
from hashlib import sha1
from setting import dbparams

conn = pymysql.Connect(**dbparams)
cursor = conn.cursor()
# 输入用户名和密码
username = input("请输入用户名：")
password = input("请输入密码：")
password = sha1(password.encode('utf8')).hexdigest()
print(username,password)

"""
注入攻击：sql注入是一种将sql代码添加到输入参数中，传递到sql服务器解析并执行一种攻击手法。
"""
# 第一种防止注入方式
# username = pymysql.escape_string(username) # excape_string 对参数中的特殊参数转意
# sql = "select uid from user where name='{}' and password='{}'".format(username,password)
# result = cursor.execute(sql)
# 第二种防止注入攻击
sql = "select uid from user where name= %s and password= %s"
print(sql)
# execute 第一个参数是sql语句 第二个参数是sql语句中包含的参数
# 形式可以是[参数1,参数2] 也可以是元祖 (参数1,参数2...)
result = cursor.execute(sql,[username,password])
print(cursor._executed)

if result>0:
    print("登录成功")
else:
    print("登录失败")

cursor.close()
conn.close()