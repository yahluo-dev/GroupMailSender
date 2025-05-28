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

# HTML content, example
html_content = """
<html>
<head>
  <style>
    body {
      color: #000000;
      font-family: Arial, sans-serif;
      font-size: 14px;
    }
    a {
      color: #000000;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <h3>Dobrý den,</h3>

  <p>píšu Vám jménem studentské organizace, abych Vám představil jeden z našich projektů – Diář studentů, který distribujeme studentům VUT a MUNI, vždy po 5 000 kusech pro každou univerzitu. Studenti za diář neplatí.</p>

  <p>Jednou z hlavních motivací je pomáhat studentům lépe zvládat a plnit termíny. Na základě našeho loňského výzkumu mezi univerzitami jsme zjistili, že tištěné médium je stále vnímáno jako důvěryhodnější a má svůj smysl i v digitální době.</p>

  <p>Jako studentská organizace se rádi prezentujeme projekty, které studentům skutečně pomáhají. V současné době hledáme inzerenty do našeho diáře – oficiální nabídku Vám zasílám v příloze.</p>

  <p>Pokud by pro Vás inzerce nebyla zajímavá, jsme otevřeni i jiným formám spolupráce, například můžeme do diáře zařadit slevový kód, kterým podpoříme Váš prodej a zároveň zvýšíme atraktivitu našeho diáře. Rádi s Vámi probereme jakékoli další možnosti či návrhy.</p>

  <p>Těším se na případnou spolupráci a jsem k dispozici k dalším diskuzím.</p>

  <p>S pozdravem,</p>
  <div dir="ltr" class="gmail_signature" data-smartmail="gmail_signature"><div dir="ltr"><div style="color:rgb(10,60,90);font-family:Verdana,Geneva,sans-serif;font-size:9.33333px;font-style:normal;font-weight:400;letter-spacing:normal;text-align:start;text-indent:0px;text-transform:none;word-spacing:0px;white-space:normal;float:left;height:116px"><a href="https://www.iaeste.cz/" title="Official page of IAESTE Czech Republic" style="background-color:transparent;color:rgb(2,117,216);text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.iaeste.cz/&amp;source=gmail&amp;ust=1748421107251000&amp;usg=AOvVaw2hL5z7Bj7KLS1rZq3cAmLt"><img alt="IAESTE Czech Republic" src="https://ci3.googleusercontent.com/meips/ADKq_NY-wrFJuXbKgL8_Dv37Bb3lBKeE8NXGqoKe5_AM0dpjrsdN4u1tnDDw57rKovqiEvhy0pEt1apOHZaoDb8zKUy3b4QgjkPsZZsu__-OcnzmV7M=s0-d-e1-ft#https://www.iaeste.cz/mail/img/logo/resized/min/brno_min.png" style="border-style:none;vertical-align:middle" class="CToWUd" data-bit="iit"></a></div><div style="color:rgb(10,60,90);font-family:Verdana,Geneva,sans-serif;font-size:9.33333px;font-style:normal;font-weight:400;letter-spacing:normal;text-align:start;text-indent:0px;text-transform:none;word-spacing:0px;white-space:normal;float:left;height:116px;width:0pt;border-width:1.5pt;border-style:solid;border-color:rgb(10,60,90);border-radius:3pt;line-height:9.33333px"></div><div style="color:rgb(10,60,90);font-family:Verdana,Geneva,sans-serif;font-size:9.33333px;font-style:normal;font-weight:400;letter-spacing:normal;text-align:start;text-indent:0px;text-transform:none;word-spacing:0px;white-space:normal;float:left;height:116px;width:180pt;margin-left:3pt"><div style="height:15pt;min-height:15pt;margin-bottom:2pt"><span style="font-size:12pt;line-height:15pt;vertical-align:text-bottom;font-weight:bold">Marek Sechra<br></span><span style="margin-left:13pt"></span></div><div style="margin-bottom:4pt"><div style="color:rgb(85,85,85)">Member of the Corporate Relations Team</div><div><a title="Phone number" style="background-color:transparent;color:inherit;text-decoration:none">+420 735 859 073<br></a></div></div><div style="height:25.5pt;width:240px;margin-bottom:4pt;text-align:left"><div style="float:left"><a href="http://maps.google.com/?q=Purky%C5%88ova+93+Brno" title="Find with Google Maps..." style="background-color:transparent;color:rgb(153,153,153);text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://maps.google.com/?q%3DPurky%25C5%2588ova%2B93%2BBrno&amp;source=gmail&amp;ust=1748421107251000&amp;usg=AOvVaw27J1CmcTf9_uUrbhWvomN0"><span style="font-weight:bold">IAESTE LC Brno</span><br><span>Purkyňova 93</span><br><span>612 00&nbsp;Brno</span></a></div><div style="float:left"><br></div><div style="float:right"><br></div><div style="float:right"><a href="https://ikariera.cz/" title="iKariera.cz" style="background-color:transparent;color:rgb(153,153,153);text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://ikariera.cz/&amp;source=gmail&amp;ust=1748421107252000&amp;usg=AOvVaw2HkPXROx_QXzeNdwOUS8kV">ikariera.cz</a><br><a href="https://projekty.iaeste.cz/" title="Projekty IAESTE" style="background-color:transparent;color:rgb(153,153,153);text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://projekty.iaeste.cz/&amp;source=gmail&amp;ust=1748421107252000&amp;usg=AOvVaw3ln5Cat8yjN1R09ifDXUN6">projekty.iaeste.cz</a></div></div><div style="margin-bottom:2pt"><a href="https://www.facebook.com/iaestebrno" title="Facebook" style="background-color:transparent;color:rgb(2,117,216);text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.facebook.com/iaestebrno&amp;source=gmail&amp;ust=1748421107252000&amp;usg=AOvVaw3YgDuclnQpWkojH0dT9I5a"><img alt="Facebook" src="https://ci3.googleusercontent.com/meips/ADKq_NbG37ksRCxwgLkBN3W8DX4nFcl21jREhVKAnitxRXwJmeecH9tqd_0_zPwxjVplVd9ZujGWJzlesZIYf_H2Q0ne8kodHqxZFO4BYRx4Mrye8-_qgdk=s0-d-e1-ft#https://www.iaeste.cz/mail/img/social_media/1/19px/facebook.png" style="border-style:none;vertical-align:text-bottom;margin-right:3pt" class="CToWUd" data-bit="iit"></a><a href="https://www.youtube.com/user/IAESTECzechRepublic" title="YouTube" style="background-color:transparent;color:rgb(2,117,216);text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.youtube.com/user/IAESTECzechRepublic&amp;source=gmail&amp;ust=1748421107252000&amp;usg=AOvVaw3dncrSgFALeFqmwFXauxWV"><img alt="YouTube" src="https://ci3.googleusercontent.com/meips/ADKq_NZfur5S7KMC4cRcYwI4IggTp_zydoktS10Eaq7vMUvJvrytXszrS8zIvfA-mOxQ4n5ho7_DRb3g4Mvu_CyfC6yF1WSNuXWqIgL9x6QI2-wmRpJFnQ=s0-d-e1-ft#https://www.iaeste.cz/mail/img/social_media/1/19px/youtube.png" style="border-style:none;vertical-align:text-bottom;margin-right:3pt" class="CToWUd" data-bit="iit"></a></div></div></div></div>
</body>
</html>
"""

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
   
for c in contacts:
    attachment_paths = [r"Diar_Studenta_VUT_Nabidka.pdf", r"Diar_Studenta_MUNI_Nabidka.pdf"] #path in same directory for both i reccomend use raw string  in python...
    # if u want u can append time.time.sleep(xy)
    send_email(c,"SENDER_EMAIL" ,'SUBJECT_STRING', html_content,attachment_paths)
    print(f"sent to: {c}")