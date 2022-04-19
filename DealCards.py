from CardDeck import *
from EmailSender import *
from GameConstants import *

"""
This file is just for actually creating the deck and players and dealing out and sending the cards
"""

players = []
deck = CardDeck(0, None)
# deck.add_power_cards(powers)
deck.shuffle()
deck.shuffle()

for email in players_numbers:
    players.append(Player(email))


deck.deal(players, 2)

for player in players:
    send_email(player)


