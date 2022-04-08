from CardDeck import *
from Player import *
from EmailSender import *


players_numbers = ["2082276546@tmomail.net", "2088816110@vtext.com"]
players: [Player] = []

for email in players_numbers:
    players.append(Player(email))

deck = CardDeck()
deck.shuffle()
deck.deal(players, 5)

for player in players:
    player.show_hand()

for player in players:
    send_email(player)
