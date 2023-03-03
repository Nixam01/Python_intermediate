import smtplib

mailFrom = 'Your automation system'
mailTo = ['marcin.latawiecc@gmail.com', 'marlatawiec01@gmail.com']
mailSubject = ''
mailBody = '''Hello

This mail confirms good processing

Bye
'''
message = '''From: {}
Subject: {} 

{}
'''.format(mailFrom, mailSubject, mailBody)

user = 'mezigamespl@gmail.com'
password = 'youtubeto'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')