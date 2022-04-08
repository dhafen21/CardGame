from CardDeck import *
from EmailSender import *

"""
This file is just for actually creating the deck and players and dealing out and sending the cards
"""


players_numbers = ["2082276546@tmomail.net", "2088816110@vtext.com"]
players = []
deck = CardDeck()
deck.shuffle()

for email in players_numbers:
    players.append(Player(email))

deck.deal(players, 5)

for player in players:
    send_email(player)
