class Player:

    def __init__(self, email: str):
        self.email = email
        self.hand = []

    def show_hand(self):
        print("Showing {}'s hand: \n".format(self.email))
        for card in self.hand:
            card.to_string()
        print('\n')