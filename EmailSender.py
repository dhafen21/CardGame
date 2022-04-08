import email.policy
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Player import *

password = "dollabills"
sender_email = "pynance2@gmail.com"


def send_email(player: Player):
    receiver_email = player.email

    message = MIMEMultipart("alternative")
    message["Subject"] = "New Hand"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "\n"

    for card in player.hand:
        text += card.get_card() + '\n'

    print(text)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

