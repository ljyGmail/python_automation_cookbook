from email.message import EmailMessage
import ssl
import smtplib
import os

email_sender = 'liangjy881@gmail.com'
email_paasword = os.environ.get('GMAIL_PWD')
# email_receiver = 'liangjy881@naver.com'
email_receiver = 'kyyang@vantus.co.kr'

subject = '浓情化不开'
body = """
情越浓，越会化不开，却清楚这是爱
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_paasword)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
