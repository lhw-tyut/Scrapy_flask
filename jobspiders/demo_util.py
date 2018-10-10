import pymysql
from logger.syslogger import logger

class DBUtils():
    def __init__(self,host='localhost',username='root',password='1234',schema='myjob',port='3306',charset='utf8'):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__port = port
        self.__schema = schema
        self.__charset = charset
        self.__conn = None
        self.__cursor = None

    def getConnection(self):
        try:
            self.__conn = pymysql.connect(self.__host,self.__username,self.__password,self.__schema,charset=self.__charset)

        except (pymysql.DatabaseError,pymysql.MySQLError,Exception):
            logger.error("数据库连接失败。。。  " + self.__host)
        self.__cursor = self.__conn.cursor()

    def execute(self,sql,param=None):
        try:
            if self.__conn and self.__cursor:
                if param:
                    self.__cursor.execute(sql,param)
                else:
                    self.__cursor.execute(sql)
        except:
            logger.error("执行语句:"+sql , str(param))
            self.__cursor.close()
            self.__conn.close()

    def executemany(self,sql,param):
        try:
            if self.__cursor and self.__conn:
                self.__cursor.executemany(sql,param)
        except:
            logger.error("执行语句:" + sql + str(param))
            self.__cursor.close()
            self.__conn.close()

    def executeQuery(self,sql,param=None,row='one'):
        try:
            if self.__cursor and self.__conn:
                self.__cursor.execute(sql,param)
                if row == 'one':
                    print(self.__cursor.fetchone())
                    return self.__cursor.fetchone()
                else:
                    return self.__cursor.fetchall()
        except:
            logger.error("执行语句:" + sql)
            self.__cursor.close()
            self.__conn.close()

    def close(self):
        if self.__conn and self.__cursor:
            self.__cursor.close()
            self.__conn.close()

    def commit(self):
        self.__conn.commit()

    def rollback(self):
        self.__conn.rollback()

    def insert(self,sql,param=None):#insert语句  插入数据
        '''
        sql = "insert into Lessor(leaccount,lepassword,lenickname,leregister)" \
              "values(%s,%s,%s,%s)"
        param = [('user01','111','包租公','2018-02-07'),
                 ('user02','222','风筝','2018-04-10'),
                 ('user03','333','天使','2018-01-01'),
                 ('user04','444','翠花','2018-04-18'),
                 ('user05','555','平头哥','2018-02-05')]

        sql1 = "insert into rentinghouse(leid,rhaddress,rharea,rhfloor,rhprice)" \
              "values(%s,%s,%s,%s,%s)"
        param1 = [(2, '北京朝阳区', 100, 2, 10000),
                 (4, '北京昌平区', 65, 3, 1000),
                 (3, '北京海淀区', 43, 23, 3000),
                 (4, '北京宣武区', 120, 14, 5000),
                 (1, '北京西城区', 90, 5, 8000)]
        '''
        self.getConnection()
        #self.executemany(sql,param)
        self.execute(sql,param)
        #logger.info("成功执行:"+sql+'  ')
        logger.info("成功执行insert语句")
        self.commit()
        self.close()

    def selectLessorallInfo(self,sql,param=None):

        self.getConnection()
        res = self.executeQuery(sql,param,row='qu')
        print(res)
        self.close()

