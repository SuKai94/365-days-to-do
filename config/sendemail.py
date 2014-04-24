#!/usr/bin/env python
# coding: utf-8
from email.mime.text import MIMEText
import smtplib
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')   

# 设置服务器以及邮箱的后缀
mail_host="smtp.exmail.qq.com"
mail_postfix="qq.com"

# 发送邮件
def send_email(mail_user,mail_pass,mail_to,sub,content):
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = mail_to
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, mail_to, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False