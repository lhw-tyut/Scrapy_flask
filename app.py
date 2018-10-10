from flask import Flask,render_template,request,session
from controller.commentspider import Commentget
from controller.getpic import Download
from controller.getpic1 import Img
from utils.pageutils import Pagination
import importlib,sys
importlib.reload(sys)
from dao.demo_util import DBUtils
from entity .user import User
from dao.userdao import UserDao
import os
from datetime import timedelta
from star import spiderThread
from star1 import spiderThread1
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
userDao = UserDao()
db = DBUtils()
citys = []
#主页
@app.route('/')
def index():
    print(session.get("userName"))
    return render_template('index.html')

#登录页面
@app.route('/log')
def log():
    return render_template('login.html')

#注册页面
@app.route('/reg')
def reg():
    return render_template('register.html')

#修改密码页面
@app.route('/alter')
def alter():
    return render_template('alterPwd.html')

#处理注册
@app.route('/register',methods=['GET','POST'])
def register():
    userName = request.form['username']
    userPwd = request.form['password']
    if userName != "" and userPwd != "":
        user = User()
        user.userName = userName
        user.userPwd = userPwd
        result = userDao.createUser(user)
    if result:
        return render_template('login.html', message="注册成功，请登录", code=500)  # 第一参数是其他的URL，message是带过去的数据
    if result:
        return render_template('register.html', message="注册失败", code=500)  # 第一参数是其他的URL，message是带过去的数据
    pass
#返回主页
@app.route('/main',methods=['GET','POST'])
def main():
    users = userDao.getAllUsers()
    return render_template('photo1.html', users=users)

#处理登录
@app.route('/login',methods=['GET','POST'])
def login():
    userName = request.form['username']
    userPwd = request.form['password']
    if userName != "" and userPwd != "":
        user = User()
        user.userName = userName
        user.userPwd = userPwd

        result = userDao.getUserByUserNameAndPwd(user)

    if result:
        session['userName'] = user.userName
        print(session['userName'])
        print(session.get("userName"))
        users = userDao.getAllUsers()
        return render_template('photo1.html', user=user, users=users)
    else:
        message = "用户名或者密码错误"
        return render_template('login.html', message=message, code=500)

#登出
@app.route('/logout')
def logout():
    session['userName']=None
    return render_template('index.html')

#处理修改密码
@app.route('/alterpwd',methods=['GET','POST'])
def alterPwd():
    userName = session.get("userName")
    userPwd = request.form['password']

    user = User()
    user.userName = userName
    user.userPwd = userPwd
    result = userDao.updateUser(user)
    if result:
        return render_template('photo1.html')
    else:
        return render_template('alterPwd.html')

#爬取评论
@app.route('/spidercomment')
def spidercomment():
    csipder = Commentget()
    csipder.save_to_txt()
    return render_template('photo1.html')
#显示评论
@app.route('/spidercomment1')
def spidercomment1():
    csipder = Commentget()
    message = csipder.movieComment()
    pager_obj = Pagination(request.args.get("page", 1), len(message), request.path, request.args, per_page_count=10)
    index_list = message[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()

    return render_template('commentitems.html',index_list=index_list, html=html)

#评论分析
@app.route('/spiderresult')
def spiderres():
    return render_template('comment.html')

#评论评价分析
@app.route('/spiderresultrate')
def spiderres1():
    return render_template('rate.html')


@app.route('/spiderliepin')
def spiderres2():
    sql = "select * from myjob where jobSource= %s"
    param = '猎聘网'
    message = db.selectallInfo(sql,param)
    pager_obj = Pagination(request.args.get("page", 1), len(message), request.path, request.args, per_page_count=10)
    index_list = message[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()

    return render_template('jobItems.html', index_list=index_list, html=html)

@app.route('/spiderqc1')
def spiderres3():
    spiderThread()
    return render_template('photo1.html')

@app.route('/spiderqc2')
def spiderres7():
    spiderThread1()
    return render_template('photo1.html')

@app.route('/spiderqc')
def spiderres6():
    sql = "select * from myjob where jobSource= %s"
    param = '前程无忧'
    message = db.selectallInfo(sql,param)
    pager_obj = Pagination(request.args.get("page", 1), len(message), request.path, request.args, per_page_count=10)
    index_list = message[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()

    return render_template('jobItems.html', index_list=index_list, html=html)


@app.route('/searchjob',methods=['GET','POST'])
def searchjob():
    sql = "select * from myjob where jobCompany= %s"


    param = request.form['jobPosition']

    message = db.selectallInfo(sql, param)
    pager_obj = Pagination(request.args.get("page", 1), len(message), request.path, request.args, per_page_count=10)
    index_list = message[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()

    return render_template('searchjob.html', index_list=index_list, html=html)

@app.route('/inputkey')
def spiderres5():
    return render_template('img.html')

@app.route('/inputkey1')
def spiderres8():
    return render_template('img1.html')


@app.route('/spiderimg',methods=['GET','POST'])
def spiderimg():
    download = Download()
    word = request.form['img']
    print(request.form['img'])
    res = download.main(word)
    if res:
        return render_template('photo1.html')

@app.route('/spiderimg1',methods=['GET','POST'])
def spiderimg1():
    img = Img('赵丽颖')
    img.run()
    return render_template('photo1.html')

#图片展示
@app.route('/photoshow')
def spiderres4():
    return render_template('photo1.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
