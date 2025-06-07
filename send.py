#!/bin/python
"""
Author: Marek Sechra
Last edit: 28.05.2025
Version: 0.02
"""

import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

from typing import Dict

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(to, cc, subject, html_content, attachment_paths):
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
    sender_email = 'name.surname@iaeste.cz'
    password = 'generated password'

    # Object of msg
    message = MIMEMultipart()
    message['From'] = 'name.surname@iaeste.cz' # Name of sender email
    message['To'] = to
    message['Cc'] = "" # copy address
    message['Subject'] = "Nabídka diářů IAESTE - LC Brno 2025"

    # HTML append to msg
    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    # Add of appendix (in same directory like this file)
    for attachment_path in attachment_paths:
        try:
            if not os.path.exists(attachment_path):
                print(f"ERROR: File {attachment_path} doesnt exist")
                continue
                
            with open(attachment_path, "rb") as attachment:
                # MIME type
                if attachment_path.lower().endswith('.pdf'):
                    part = MIMEBase('application', 'pdf')
                else:
                    part = MIMEBase('application', 'octet-stream')
                
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                filename = os.path.basename(attachment_path)
                
                # Content header for pdf
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{filename}"'
                )
                # Backup-way
                part.add_header('Content-Type', f'application/pdf; name="{filename}"')
                
                message.attach(part)
        except Exception as e:
            print(f"CHYBA při přidávání přílohy {attachment_path}: {e}")


    # Connect to SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        # Make of list of reciepients
        recipients = [to]
        if cc:
            recipients.append(cc)

        server.sendmail(sender_email, recipients, message.as_string())

def main(contacts_path: str, message_path: str, attachment_paths: list[str]):

    with open(message_path) as f:
        message = f.read()

    with open(contacts_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"Firma: {row['firma']}")
            print(f"Email: {row['email']}")

            send_email(row['email'], "SENDER_EMAIL", 'SUBJECT_STRING', message,
                       attachment_paths)
            print(f"sent to: {row['email']}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: send.py <message_file> <contacts_file> " +
              "[attachment_1], ... [attachment_n]")
        sys.exit(1)

    message_path = sys.argv[1]
    contacts_path = sys.argv[2]     # Kontakty ve tvaru
                                    # firma,email
                                    # firma1,firma1@email.com
                                    # ...
    attachment_paths = sys.argv[3:]

    print("message:" + message_path)
    print("contacts:" + contacts_path)
    print("atts:")
    print(attachment_paths)

    main(contacts_path, message_path, attachment_paths)
