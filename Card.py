class Card:

    def __init__(self, suit: str, face_value: int, power: str = None):
        """
        Initializes a single card
        :param suit: String that represents the suit of the card (Hearts, clubs, etc...)
        :param face_value: Numeric value for the card
        :param power: Special powers the card has
        """
        self.suit = suit
        self.face_value = face_value
        self.power = power

    def to_string(self):
        """
        prints the suit and power of the card
        :return:
        """
        print(self.get_card())

    def get_card(self):
        if self.power is not None:
            return "Suit: {}, Face Value: {}, Power: {}".format(self.suit, self.face_value, self.power)
        else:
            return "Suit: {}, Face Value: {}".format(self.suit, self.face_value)
