import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Player import *


def send_email(player: Player):
    """
    Sends each player's hand as a text to that player
    :param player: Player object that stores the hand and the phone number the hand is being sent to
    :return:
    """

    password = "dollabills"
    sender_email = "pynance2@gmail.com"
    receiver_email = player.email

    message = MIMEMultipart("alternative")
    message["Subject"] = "New Hand"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "\n"

    for card in player.hand:
        text += card.get_card() + '\n'

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

