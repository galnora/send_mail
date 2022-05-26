import smtplib
import getpass
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'bojack.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')
msg.attach(p)

msg['From'] = input ("From:")
password = getpass.getpass(prompt = "Enter your password")
msg['To'] = input("To:")
msg['Subject'] = 'helo'
text = msg.as_string()


server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'],password)
server.sendmail(msg['From'], msg['To'], text)
server.quit()












# 