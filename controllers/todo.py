#!/usr/bin/env python
# coding: utf-8
import web
from config import settings, sendemail
from datetime import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

render = settings.render
db = settings.db
tb = 'todo'
user ='user'

'''
former is_login? version
'''
# def logged():
#     if web.config._session.login == 1:
#         return True
#     else:
#         return False

'''
now is_login? version, using decorator
'''
def is_login(func):
    def wrapper(*args):
        if web.config._session.login == 1:
            return func(*args)
        else:
            raise web.seeother('/')
    return wrapper

def judge_same(userid):
    if web.config._session.userid == userid:
        return True
    else:
        return False

def get_by_id(id):
    s = db.select(tb, where='id=$id', vars=locals())
    if not s:
        return False
    return s[0]

class New:
    @is_login
    def POST(self, userid):
        # if not logged():
        #     return render.error('已经登出,请重新登录', '/')
        if not judge_same(int(userid)):
            return render.error('不允许访问', '/365days/%d' % web.config._session.userid)
        i = web.input()
        title = i['title']
        content = i['content']
        if not title:
            return render.error('标题是必须的', None)
        db.insert(tb, title=title, content=content, post_date=datetime.now(), userid=userid)
        raise web.seeother('/365days/%s' % userid)

class Finish:
    @is_login
    def GET(self, userid, id):
        # if not logged():
        #     return render.error('已经登出,请重新登录', '/')
        if not judge_same(int(userid)):
            return render.error('不允许访问', '/365days/%d' % web.config._session.userid)
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        status = i.get('status', 'yes')
        if status == 'yes':
            finished = 1
        elif status == 'no':
            finished = 0
        else:
            return render.error('您发起了一个不允许的请求', '/')
        db.update(tb, finished=finished, where='id=$id', vars=locals())
        raise web.seeother('/365days/%s' % userid)

class Detail:
    @is_login
    def GET(self, userid, id):
        # if not logged():
        #     return render.error('已经登出,请重新登录', '/')
        if not judge_same(int(userid)):
            return render.error('不允许访问', '/365days/%d' % web.config._session.userid)
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        return render.detail(todo, userid)

class Edit:
    @is_login
    def GET(self, userid, id):
        # if not logged():
        #     return render.error('已经登出,请重新登录', '/')
        if not judge_same(int(userid)):
            return render.error('不允许访问', '/365days/%d' % web.config._session.userid)
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        return render.todo.edit(todo, userid)

    def POST(self, userid, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        title = i['title']
        content = i['content']
        if not title:
            return render.error('标题是必须的', None)
        db.update(tb, title=title, content=content,  where='id=$id', vars=locals())
        return render.error('修改成功！', '/365days/%s' % userid)

class Delete:
    @is_login
    def GET(self, userid, id):
        # if not logged():
        #     return render.error('已经登出,请重新登录', '/')
        if not judge_same(int(userid)):
            return render.error('不允许访问', '/365days/%d' % web.config._session.userid)
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        db.delete(tb, where='id=$id', vars=locals())
        return render.error('删除成功！', '/365days/%s' % userid)

class Index:
    @is_login
    def GET(self, userid):
        # if not logged():
            # return render.error('已经登出,请重新登录', '/')
        if not judge_same(int(userid)):
            return render.error('不允许访问', '/365days/%d' % web.config._session.userid)
        todos1 = db.select(tb, where='userid=$userid', order='finished asc, id asc', vars=locals())
        todos2 = db.select(tb, where='userid=$userid', order='finished asc, id asc', vars=locals())
        return render.index(todos1, todos2, userid)

class Email:
    @is_login
    def GET(self, userid, id):
        # if not logged():
        #     return render.error('已经登出,请重新登录', '/')
        if not judge_same(int(userid)):
            return render.error('不允许访问', '/365days/%d' % web.config._session.userid)
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        return render.todo.sendemail(todo, userid)

    def POST(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        mail_user = i['mail_user']
        mail_pass = i['mail_pass']
        mail_to = i['mail_to']
        sub = i['sub']
        content = i['content']
        sendemail.send_email(mail_user,mail_pass,mail_to,sub,content)
        return render.error('邮件发送成功！', '/365days/%s' % userid)

class AddUser:
    def GET(self):
        return render.adduser()
    
    def POST(self):
        i = web.input()
        username = i['username']
        pwd = i['password']
        if not username:
            return render.error('请填写用户名！','/')
        if not pwd:
            return render.error('请填写密码！','/')
        check = db.select(user, what='username', where='username=$username', vars=locals())
        if check:
            return render.error('用户名已经被占用！','/')
        db.insert(user, username=username, pwd=pwd)
        return render.error('注册成功！','/')

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        i = web.input()
        username = i['username']
        pwd = i['password']
        if not username:
            return render.error('请填写用户名！','/')
        if not pwd:
            return render.error('请填写密码！','/')
        check = db.select(user, what='pwd', where='username=$username', vars=locals())
        if not check:
            return render.error('用户名不存在!','/')
        check = check[0]['pwd']
        if check != pwd:
            return render.error('密码错误！','/')
        userid = db.select(user, what='userid', where='username=$username', vars=locals())
        userid = userid[0]['userid']
        web.config._session.login = 1
        web.config._session.userid = userid
        raise web.seeother('/365days/%d' % userid)

class Logout:
    def GET(self):
        web.config._session.login = 0
        web.config._session.userid = '0'
        raise web.seeother('/')