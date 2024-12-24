#Fraud detection email alert logic

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(to_email, subject, body):
    from_email = 'ishansheth.8120@gmail.com'
    password = 'Ishan@Jack8120'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_email,password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()



