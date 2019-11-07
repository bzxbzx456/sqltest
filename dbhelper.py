import pymysql

class DBHelper:
    def __init__(self,params):
        """
        :param params: 链接参数字典
        """
        self.conn = pymysql.Connect(**params)  # 创建链接对象
        self.init_param()   # 初始化sql字典
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)  # 创建游标并以字典显示
    def __del__(self):
        self.cursor.close() # 关闭游标对象
        self.conn.close()  # 关闭链接对象
    def init_param(self):
        # sql语句字典
        self.params = {
            'fields': '*',
            'tables': '',
            'WHERE': '',
            'GROUPBY': '',
            'HAVING': '',
            'ORDERBY': '',
            'LIMIT': ''
        }
        # 逻辑与的链接
    def where(self,**kwargs):
        """
        生成查询条件
        :param kwargs: 参数字典：{‘name’：‘tom’，‘age’：30}
                       name='tom' and age=30
        :return:
        """
        #运算符字典
        ops = {
            'ne':'!=',
            'gt':'>',
            'ge':'>=',
            'lt':'<',
            'le':'<=',
            'contains':'like',
            'in':'in',
            'nin':'not in'
        }
        result = " where "
        for key in kwargs: # 遍历条件
            keys = key.split('__') # 以__爽下划线做分割
            if len(keys)>1: #  如果长度大于1
                op = ops[keys[1]] # op 取第二个符号
                if isinstance(kwargs[key],str):  # 判断如果你的key是字符串
                    result += keys[0] + op +"'" + pymysql.escape_string(kwargs[key]) + "' and " # 拼接起并把key写成字符串赋值给result
                else:
                    result += keys[0] + op + kwargs[key] + 'and' # 不是字符串就不加引号赋值
            else: # 另外长度不大于1
                if isinstance(kwargs[key],str): # 判断如果你的key是字符串
                    result += keys[0] + "= '" + pymysql.escape_string(kwargs[key]) + "' and " # 拼接起并把key写成字符串赋值给result
                else:
                    result += keys[0] + '= '+ kwargs[key] + 'and'# 不是字符串就不加引号赋值

        result = result.strip(' and ') # 去掉最后拼接完最后的and
        self.params['WHERE'] = result   # 用result替换 WHERE
        return self  # 返回

    def whereor(self,**kwargs):
        """
        生成查询条件
        :param kwargs: 参数字典：{‘name’：‘tom’，‘age’：30}
                       name='tom' and age=30
        :return:
        """
        #运算符字典
        ops = {
            'ne':'!=',
            'gt':'>',
            'ge':'>=',
            'lt':'<',
            'le':'<=',
            'contains':'like',
            'in':'in',
            'nin':'not in'
        }
        result = " where "
        for key in kwargs: # 遍历条件
            keys = key.split('__') # 以__爽下划线做分割
            if len(keys)>1: #  如果长度大于1
                op = ops[keys[1]] # op 取第二个符号
                if isinstance(kwargs[key],str):  # 判断如果你的key是字符串
                    result += keys[0] + op +"'" + pymysql.escape_string(kwargs[key]) + "' or " # 拼接起并把key写成字符串赋值给result
                else:
                    result += keys[0] + op + kwargs[key] + 'or' # 不是字符串就不加引号赋值
            else: # 另外长度不大于1
                if isinstance(kwargs[key],str): # 判断如果你的key是字符串
                    result += keys[0] + "= '" + pymysql.escape_string(kwargs[key]) + "' or " # 拼接起并把key写成字符串赋值给result
                else:
                    result += keys[0] + '= '+ kwargs[key] + 'or'# 不是字符串就不加引号赋值

        result = result.strip(' or ') # 去掉最后拼接完最后的and
        self.params['WHERE'] = result   # 用result替换 WHERE
        return self  # 返回

    def table(self,tables):    #获取查询结果
        self.params['tables'] = tables
        return self

    # 排序
    def orderby(self,params):
        """
        :param params: 排序字符串,"name asc,age desc"
        :return:
        """
        self.params["ORDERBY"] = "order by {}".format(params)
        return self

    # 限制结果集
    def limit(self,params):
        self.params["LIMIT"] = "limit {}".format(params)
        return self

    def groupby(self,params):
        self.params["GROUPBY"] = "group by {}".format(params)
        return self

    def fields(self,fields):
        self.params['fields'] = fields
        return self

    def having(self,**kwargs): # 与where一样。
        ops = {
            'ne': '!=',
            'gt': '>',
            'ge': '>=',
            'lt': '<',
            'le': '<=',
            'contains': 'like',
            'in': 'in',
            'nin': 'not in'
        }
        result = " having "
        for key in kwargs:  # 遍历条件
            keys = key.split('__')  # 以__爽下划线做分割
            if len(keys) > 1:  # 如果长度大于1
                op = ops[keys[1]]  # op 取第二个符号
                if isinstance(kwargs[key], str):  # 判断如果你的key是字符串
                    result += keys[0] + op + "'" + pymysql.escape_string(
                        kwargs[key]) + "' and "  # 拼接起并把key写成字符串赋值给result
                else:
                    result += keys[0] + op + kwargs[key] + 'and'  # 不是字符串就不加引号赋值
            else:  # 另外长度不大于1
                if isinstance(kwargs[key], str):  # 判断如果你的key是字符串
                    result += keys[0] + "= '" + pymysql.escape_string(kwargs[key]) + "' and "  # 拼接起并把key写成字符串赋值给result
                else:
                    result += keys[0] + '= ' + kwargs[key] + 'and'  # 不是字符串就不加引号赋值

        result = result.strip(' and ')  # 去掉最后拼接完最后的and
        self.params['HAVING'] = result  # 用result替换 WHERE
        return self  # 返回

    #获取查询结构
    def select(self):
        # 初始化spl语句
        sql = "SELECT {fields} FROM {tables} {WHERE} {GROUPBY} {HAVING} {ORDERBY} {LIMIT}"
        # sql语句里的条件全部用初始化的sql字典替换
        sql = sql.format(**self.params) #格式化
        print(sql) # 输出sql语句
        self.sql = sql
        return self.query(sql)

    def query(self,sql):   #执行原生sql语句
        self.init_param()  # 还原查询参数字典，不受上一次查询影响
        try:
            self.cursor.execute(sql) # 执行sql语句
            return self.cursor.fetchall()  #返回全部游标
        except Exception as e:
            print(e)
            return None



    # 修改记录
    def update(self,**kwargs):
        """
        :param kwargs: sname='tom',sage=20 ==> 'sname='tom','sage'=20'
        :return:
        """
        #1.把参数值是字符串的两边添加单引号，并且转意
        kwargs = {key:"'" +value+"'" if isinstance(value,str) else value for key,value in kwargs.items()}
        #2.把键值对变成字符串
        res = ','.join([key+"="+str(value) for key,value in kwargs.items()])
        self.params['KRYVALUE'] = res
        sql = "UPDATE {tables} SET {KEYVALUE} {WHERE}".format(**self.params)
        print(sql)
        return self.excute(sql)
    def excute(self,sql):
        self.sql = sql
        self.init_param()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

    """
    db.getByxxx()
    db.count()
    """
if __name__ == '__main__':
    from setting import dbparams  # 导入数据库
    db = DBHelper(dbparams)  #初始化db
    # print(db.conn)
    # print(db.params)
    # date = db.table('student').fields('sname,sclass').select()
    # print(date)
    date1 = db.table('student').where(sclass__ne='95033').select()
    print(date1)