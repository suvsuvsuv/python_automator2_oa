# -*- coding: utf-8 -*-
# #coding=utf-8 要写在文件最开始！ 长记性了！ 谢谢大家的帮助！
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
import imaplib

#receiver = '1043990501@qq.com'
receiver = '1833213932@qq.com'
mail_title = 'automate checkin'
sender_qq = '1833213932'


# https://www.zybuluo.com/rickyChen/note/362077
def send_mail(sender_qq='',pwd='', receiver='',mail_title='',mail_content='', file_name=None):
    host_server = 'smtp.qq.com'
    sender_qq_mail = sender_qq+'@qq.com'

    #ssl login
    smtp = SMTP_SSL(host_server)
    #set_debuglevel() 1- on, 0 - off
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login( sender_qq, pwd)

    msg = MIMEMultipart('related')
    msgText = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    if file_name != None:
        att = MIMEText(open('%s' % file_name, 'rb').read(), 'base64', 'utf-8')  # 添加附件
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name
        msg.attach(att)
    else:
        msg.attach(msgText)
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()


import smtplib

sender = '1043990501@qq.com'#发件人地址
receiver = '1043990501@qq.com'#收件人地址
smtpserver = 'smtp.qq.com'#邮件服务器
smtp = smtplib.SMTP_SSL()
def send_email(username, password, mail_title='', mail_content='', file_name=None):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header(mail_title, 'utf-8')
    msgRoot["From"] = 'auto_checkin'
    msgText = MIMEText('%s'%mail_content,'html','utf-8')#你所发的文字信息将以html形式呈现
    msgRoot.attach(msgText)
    exception = False
    if file_name is not None:
        try:
            att = MIMEText(open('%s'%file_name, 'rb').read(), 'base64', 'utf-8')#添加附件
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"'%file_name
            msgRoot.attach(att)
        except:
            exception = True
            print(file_name + " is not found" ) # 登录失败
    if not exception:
        print("send qq mail: " + mail_content)
        smtp = SMTP_SSL(smtpserver)
        # set_debuglevel() 1- on, 0 - off
        smtp.set_debuglevel(0)
        smtp.ehlo(smtpserver)
        sender_qq = "1833213932@qq.com"
        password = "rtrpkhdjjaatfdhd"
        smtp.login(sender_qq, password)
        smtp.sendmail(sender_qq, receiver, msgRoot.as_string())
        smtp.quit()
        '''num = 0;
        while num <= 3:  # 持续尝试发送，直到发送成功
            try:
                print "send qq mail"
                smtp.sendmail(sender, receiver, msgRoot.as_string())  # 发送邮件
                break
            except:
                try:
                    smtp.connect(smtpserver)  # 连接至邮件服务器
                    smtp.login(sender_qq, password)  # 登录邮件服务器
                except:
                    print "failed to login to smtp server"  # 登录失败
            num = num + 1
            '''

EMAIL_FOLDER = "inbox"

import re
import email
import datetime
from hashlib import md5
#http://www.pythoner.com/414.html
from datetime import datetime
def imap4(host, port, usr, pwd, use_ssl):
    """Imap4 handler

    :param host: host
    :param port: port
    :param usr: username
    :param pwd: password
    :param use_ssl: True if use SSL else False
    """
    cmd = None
    # Connect to mail server
    try:
        conn = imaplib.IMAP4_SSL(host, port) if use_ssl else imaplib.IMAP4(host, port)
        conn.login(usr, pwd)
        # http://blog.csdn.net/q932104843/article/details/52502447
        # conn.select("INBOX", readonly=False)
        conn.select(EMAIL_FOLDER, readonly=False)
        # rv, data = conn.search(None, "ALL")
        rv, data = conn.search(None, '(UNSEEN)')
    except BaseException as e:
        #exit_script("Connect to {0}:{1} failed".format(host, port), e)
        print(datetime.now(), "failed to login")
        return cmd

    if rv != 'OK':
        print ("No messages found!")
        return cmd

    list = data[0].split()
    #for num in data[0].split():
    i = len(list)
    while i > 0: # 返回列表按倒序排列
        num = list[i -1]
        rv, data = conn.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            break

        conn.store(num, '+FLAGS', '\Seen')

        # http://blog.csdn.net/q932104843/article/details/52502447
        #msg = email.message_from_string(data[0][1])
        #decode = email.header.decode_header(msg['Subject'])[0]
        #subject = unicode(decode[0])

        try:
            msg = email.message_from_string(data[0][1].decode('utf-8', errors='replace'))
            sub = msg.get('subject')
            subdecode = email.header.decode_header(sub)[0][0]
            subject = subdecode #subdecode.decode('utf-8').strip().lower()
            print ('Message %s: %s' % (num, subject))
            if subject.find("oa:") != -1: # 中文标题会抛异常
                strlist = subject.split(':')
                if len(strlist) >= 2:
                    cmd = strlist[1]
                    print('command: %s' % (cmd))
                    return cmd

        except UnicodeDecodeError as e:
            print(e)
        except UnicodeEncodeError as e:
            print(e)
        except:
            #subject = subdecode.decode('utf-8').strip().lower()
            print('unknonw chinese', subject)
        i -= 1

    # Logout this account
    conn.logout()
    return cmd

from appConstants import *
if __name__ == "__main__":
    cmd = imap4("imap.qq.com", 993, RECEIVE_IMAP_USER, RECEIVE_IMAP_PWD, True)
    print('command: %s' % (cmd))
