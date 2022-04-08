from Card import Card
from Player import *
import random


class CardDeck:

    def __init__(self, num_players: int = 4, suits=None, number_range: range = range(1, 6)):
        """
        Initializes the deck of cards
        :param num_players: the number of players in the game. Determines the number of duplicates that each card will have
        :param suits: The suits used in the game (Green & Red, or Spades, Clubs, Hearts Diamonds, etc)
        :param number_range: The range of values for the cards used in the game
        """

        if suits is None:
            suits = ["Green", "Red"]
        self.suits = suits
        self.number_range = number_range
        self.num_players = num_players
        self.deck: [Card] = []

        for suit in self.suits:
            for val in self.number_range:
                for player in range(self.num_players):
                    self.deck.append(Card(suit, val))

    def print_deck(self) -> None:
        """
        Prints the deck as it is currently stored
        :return: Returns nothing
        """

        for card in self.deck:
            card.to_string()

    def shuffle(self):
        """
        shuffles and updates the order of the deck so it is randomized
        :return:
        """
        new_deck = []
        while len(self.deck) > 0:
            new_deck.append(self.deck.pop(random.randint(0, len(self.deck) - 1)))
        self.deck = new_deck

    def deal(self, players: [Player], num_cards_per_player: int = None):
        if num_cards_per_player is not None:
            for i in range(num_cards_per_player):
                for player in players:
                    player.hand.append(self.deck.pop())
        else:
            while len(self.deck) > 0:
                for player in players:
                    if len(self.deck) == 0:
                        break
                    player.hand.append(self.deck.pop())

