from email.message import EmailMessage
import ssl
import smtplib
from app import password

email_sender = 'htethlaingwin2022@gmail.com'
email_password = password

email_receiver = 'htethlaingwin.bdm29@gmail.com'

subject = "Don't forget the lunch"
body = """
 When you leave the house, don't forget to lock the door...!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
