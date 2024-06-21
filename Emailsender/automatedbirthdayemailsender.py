from email.message import EmailMessage
import csv
from datetime import datetime
from app2 import password
import ssl
import smtplib

# Email credentials and recipient
email_sender='morrisindet@gmail.com'
email_password = password


# Email subject and body 
def send_birthday_email(name,email):
    subject = 'Birthday wishes from Morris Sindet'
  
  
    body = f'Happy birthday  {name}  May your day be filled with Joy and blessings in abundance'
  
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email
    em['Subject'] = subject
    em.set_content(body)
 #  Create SSL context

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email, em.as_string())

today = datetime.today().strftime('%Y-%m-%d')

with open('birthdays.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['birthday'] == today:
            send_birthday_email(row['name'], row['email'])
