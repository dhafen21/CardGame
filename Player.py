class Player:
    """
    Class for a single player in a game that can hold a hand
    """

    def __init__(self, email: str):
        """
        Initializes the current player with an email to send the hand to and the hand dealt to them
        :param email: The email/phone number for that current player
        """
        self.email = email
        self.hand = []

    def show_hand(self):
        """
        Prints the hand of the current player
        :return:
        """
        print("Showing {}'s hand: \n".format(self.email))
        for card in self.hand:
            card.to_string()
        print('\n')