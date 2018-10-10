from .demo_util import DBUtils

from entity.user  import User
class UserDao(DBUtils):
    #根据用户名和密码进行查询
    def getUserByUserNameAndPwd(self,user):
        sql = "select username,userpwd from user where username=%s and userpwd=%s"
        param = (user.userName, user.userPwd)
        result = super().selectoneInfo(sql, param)
        return result

    #查询所有用户信息
    def getAllUsers(self):
        sql = "select * from user"
        result = super().selectallInfo(sql)

        return result

    def createUser(self,user):
        sql = "insert into user(username,userpwd) values(%s,%s) "
        param = (user.userName, user.userPwd)
        res = super().insert(sql,param)
        return res

    def updateUser(self, user):
        sql = "update user set userpwd=%s where username=%s "
        param = (user.userPwd,user.userName)
        res = super().insert(sql, param)
        return res