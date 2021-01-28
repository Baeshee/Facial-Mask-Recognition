import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(foto):
    port = 587
    smtp_server = "smtp.gmail.com"
    password = "GuitarGuy997"
    sender_email = "testingpythonsendemail@gmail.com"
    receiver_email = input("Enter receiver email adress: ")
    subject = "Person without mouth mask"
    body = "The following person is walking around the complex without a mouth mask, I would kindly ask the floor patrol to approach this individual and ask them to wear one or leave the complex."

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))
    filename = foto

    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header("Content-Disposition", f"attachment; filename={filename}",)

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
