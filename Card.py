class Card:
    """
    Class for describing a single card in a game
    """

    def __init__(self, suit: str, face_value: int or None, power: str = None):
        """
        Initializes a single card
        :param suit: String that represents the suit of the card (Hearts, clubs, etc...)
        :param face_value: Numeric value for the card
        :param power: Special powers the card has
        """
        self.suit = suit
        self.face_value = face_value
        self.power = power

    def print_card(self):
        """
        prints the suit and power of the card
        :return:
        """
        print(self.to_string())

    def to_string(self) -> str:
        """
        Gets the string representation for a single card including the suit, value, and power
        :return: String description for the current card
        """

        if self.power is not None and self.face_value is not None:
            return "Suit: {}, Face Value: {}, Power: {}".format(self.suit, self.face_value, self.power)
        elif self.power is not None:
            return "Power: {}".format(self.power)
        elif self.face_value is not None:
            return "Suit: {}, Face Value: {}".format(self.suit, self.face_value)

