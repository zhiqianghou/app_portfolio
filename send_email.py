import smtplib, ssl


host = "smtp.gmail.com"
port = 465

username = "houzh.py@gmail.com"
password = "jzeoweetjbcjccxj"

receiver = "houzh.py@gmail.com"
context = ssl.create_default_context()
message = """\
Subject: Hi!
Test email sending and receiving from web app """

with smtplib.SMTP_SSL(host, port, context=context) as server:
	server.login(username, password)
	server.sendmail(username, receiver, message)
