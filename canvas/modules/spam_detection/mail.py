import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from canvas.models.canvas import CanvasDataToSend


sender_email = 'imgorlaks@gmail.com'
receiver_email = 'imgorlaks@gmail.com'
password = 'dragondesert.123.6'


def send_mail(data: CanvasDataToSend):
    SUBJECT = "New project idea"
    FROM = sender_email
    TO = receiver_email
    text = data.data[0]['content']

    BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
    ))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, BODY
        )