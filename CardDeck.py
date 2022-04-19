from Card import Card
from Player import *
import random


class CardDeck:
    """
    Class representing a deck of Card objects, can perform different acts to the deck of cards including
    deck creation, shuffling, and dealing out the cards to a list of Player objects
    """

    def __init__(self, num_players: int = 4, suits: object = None, number_range: range = range(1, 6)):
        """
        Initializes the deck of cards
        :param num_players: the number of players in the game. Determines the number of
        duplicates that each card will have
        :param suits: The suits used in the game (Green & Red, or Spades, Clubs,
        Hearts Diamonds, etc)
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
        print("A {} card deck was created".format(len(self.deck)))

    def add_power_cards(self, powers: {str: int}) -> None:
        """
        Adds wild or power cards to the deck
        :param powers: Dictionary that stores the power of the card as an index, and the number of duplicates of that
        card. Ex. {"Double Points": 2}
        :return: None
        """
        print("Adding power cards to the deck")
        for power in powers:
            for i in range(powers[power]):
                self.deck.append(Card("Power", None, power))

    def print_deck(self) -> None:
        """
        Prints the deck as it is currently stored
        :return: Returns nothing
        """

        for card in self.deck:
            card.to_string()

    def shuffle(self):
        """
        shuffles and randomizes the order of the deck
        :return:
        """
        new_deck = []
        while len(self.deck) > 0:
            new_deck.append(self.deck.pop(random.randint(0, len(self.deck) - 1)))
        self.deck = new_deck
        print("Shuffled the deck")

    def deal(self, players: [Player], num_cards_per_player: int = None):
        """
        Deals the cards into the hands of each of the players. If number of cards is provided, then each player
        receives that number of cards. If not, the cards are distributed until no cards remain in the deck
        :param players: Array of player object that are receiving the cards in their hands
        :param num_cards_per_player: The number of cards each player receives
        :return:
        """
        print("Dealing cards")
        if num_cards_per_player is not None:
            for i in range(num_cards_per_player):
                for player in players:
                    if len(self.deck) > 0:
                        player.hand.append(self.deck.pop())
                    else:
                        print("There are not enough cards to give every player {} cards".format(num_cards_per_player))
                        return
        else:
            while len(self.deck) > 0:
                for player in players:
                    if len(self.deck) == 0:
                        break
                    player.hand.append(self.deck.pop())
