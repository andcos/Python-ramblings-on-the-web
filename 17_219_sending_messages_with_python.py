# Project: send email from Python
# Input: fill in the data in the program. to and from


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andreea'
email['to'] = '<to email address>' 
email['subject'] = 'This is just your lucky day!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<your email address>', '<your password>')
  smtp.send_message(email)
  print('this message was sent ' & strtime() &'!')