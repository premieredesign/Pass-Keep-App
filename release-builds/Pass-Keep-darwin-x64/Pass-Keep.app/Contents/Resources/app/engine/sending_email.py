import smtplib, ssl
import sys
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = sys.argv[1]
password = sys.argv[2]

subject = "Here are your password(s) | Pass_Keep"
body = "Please see attachments"
message = MIMEMultipart()
message["From"] = 'Pass_Keep'
message["To"] = sender_email
message["Subject"] = subject
message["Bcc"] = sender_email
message.attach(MIMEText(body, "plain"))

def who_am_i():
    return os.popen('whoami').read().strip()

def email_it(sender_email, password):
    file_name = f"/Users/{who_am_i()}/desktop/.pass_keep_private.txt"
    with open(file_name, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file_name}",
    )
    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, sender_email, text)


print(email_it(sender_email, password))
sys.stdout.flush()
