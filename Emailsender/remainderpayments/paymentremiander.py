import os 
from email.message import EmailMessage
from email.utils import formataddr
import smtplib
# from app import password
import ssl

email_sender='morrisindet@gmail.com'
email_password = 'wzan rogv kaav xlmr'
subject = 'Invoice Remainder '

def send_email(name,email_receiver,due_date,invoice_no,amount ):
    
    # Base text message 
    em = EmailMessage()
    em['Subject']= subject
    em['From']= formataddr(('Coding is Fun corp.',f'{email_sender}'))
    em['To']= email_receiver
    em['BCC']= email_sender
    
   
    em.set_content (f'''\
        Hi {name},
        I hope you are well.
        I just want to drop you a quick reminder you that {amount} USD in respect  of our 
        invoice {invoice_no} is due for payment on {due_date}.
        I would be really grateful if you could confirm that everything is on track for payment.
        Best regards 
        Morris Sindet CEO 
        '''
    )
    em.add_alternative(f"""\
        <html>
           <body>
             <p>Hi {name},</p
             <p>I hope you are well.</p>
             <p>I just want to drop you a quick reminder you that <strong> {amount} </strong> USD in respect  of our 
                invoice {invoice_no} is due for payment on <strong>{due_date}</strong>.</p>
             <p>I would be really grateful if you could confirm that everything is on track for payment.</p>
             <p>Best regards </p 
             <p>Morris Sindet CEO </p>
            </body>
        </html>
            """ ,
                 subtype = 'html'
    )
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


# To make it run on script and not make it imported 
if __name__ == "__main__":
    send_email(
        name="John doe ",
        email_receiver='lereko4539@egela.com',
        due_date='11 Aug 2022',
        invoice_no='inv-21-12-009',
        amount='5'
    )
    