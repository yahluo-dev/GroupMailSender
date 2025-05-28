#!/bin/python
"""
Author: Marek Sechra
Last edit: 28.05.2025
Version: 0.02
"""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

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

contacts = [
    "objednavky@foractiv.cz",
    "velkoobchod@foractiv.cz",
    "info@healthyco.cz",
    "brustik@healthyco.cz",
    "obchod@potraviny-ke-zdravi.cz",
    "jorka.jorkova@gmail.com",
    "info@freshprotein.cz",
    "velkoobchod@protein.cz",
    "hr@fit-pro.cz",
    "l-stefankova@volny.cz",
    "info@gymbeam.cz",
    "pr@gymbeam.cz",
    "obchod@czc.cz",
    "obchod@alza.cz",
    "info@gamefan.cz",
    "partneri@rohlik.cz",
    "marketing.czechia@wolt.com",
    "cz-food@bolt.eu",
    "partneri@damejidlo.cz",
]

if __name__ == "__main__":
    with open("message.html") as f:
        html_content = f.read()
    for c in contacts:
        attachment_paths = [r"Diar_Studenta_VUT_Nabidka.pdf", r"Diar_Studenta_MUNI_Nabidka.pdf"] #path in same directory for both i reccomend use raw string  in python...
        # if u want u can append time.time.sleep(xy)
        send_email(c,"SENDER_EMAIL" ,'SUBJECT_STRING', html_content,attachment_paths)
        print(f"sent to: {c}")
