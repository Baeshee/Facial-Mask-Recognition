import getpass
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = ""
password = ""
receiver_email = ""


def sendMail(foto):
    port = 587
    smtp_server = "smtp.gmail.com"
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


def setEmailData():
    global sender_email
    global receiver_email

    # Set your 2 email addresses in this file to prevent entering them each time.
    emails = open('EmailSettings.txt').readlines()
    if len(emails) > 2:
        if "@gmail.com" in emails[1] and "@" in emails[2]:
            askPassword()
            sender_email = emails[1]
            receiver_email = emails[2]
            return

    sender_email = input("Enter your Sender (GMAIL) Email: ")  # hier komt je email address
    askPassword()
    receiver_email = input("Enter the Receiver Email: ")  # hier komt de receiver email address


def askPassword():
    global password
    # Go to 'Edit Configurations' (Next to RUN button) and then select 'Emulate terminal in output console'.
    # This must be set in script calling setEmailData() [Main], otherwise it WON'T ask/appear!
    password = getpass.getpass(prompt="Enter your Sender (GMAIL) Password: ")
