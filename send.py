"""
Author: Marek Sechra
Last edit: 19.12.2024
Version: 0.01
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(to, cc, subject, html_content, attachment_path):
    """
    Sending email by parametrs
    to - receiver email
    cc - copu of receiver
    subject - subject of email
    html_content - like a multi line string
    attachment_path - path to file 
    """

    # SMTP server setup
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 # port of SMTP
    sender_email = 'name.surname@email.com'
    password = 'Your_gmail_password'

    # Object of msg
    message = MIMEMultipart()
    message['From'] = 'sender@email.com' # Name of sender email
    message['To'] = to
    message['Cc'] = cc # copy address
    message['Subject'] = subject

    # HTML append to msg
    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    # Add of appendix (in same directory like this file)
    #with open(attachment_path, "rb") as attachment:
    #    part = MIMEBase('application', 'octet-stream')
    #    part.set_payload(attachment.read())
    #    encoders.encode_base64(part)
    #    filename = os.path.basename(attachment_path)
    #    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    #    message.attach(part)

    # Connect to SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        # Make of list of reciepients
        recipients = [to]
        if cc:
            recipients.append(cc)

        server.sendmail(sender_email, recipients, message.as_string())

# HTML content, example
html_content = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="cs">
    <head>
        <meta charset="UTF-8"><meta content="width=device-width, initial-scale=1" name="viewport">
    </head>
    <body>
    <h1>Test heading H1</h1>
    <bstyle="color:blue">Hello world!</b>
    </body></html>
"""

with open('emaily.csv', 'r') as file: 
    # in csv file i expect one email on one line
    f = csv.reader(file) # open csv file
    for receiver in f:
        #I expect on every line just one email
        attachment_path = r"attachment.pdf" #path in same directory for both i reccomend use raw string  in python...

        # if u want u can append time.time.sleep(xy)

        send_email(receiver[0],"SENDER_EMAIL" ,'SUBJECT_STRING', html_content,attachment_path)

        # On the last iteration i will make Index error because of EndOfFile, but its not important...

   

