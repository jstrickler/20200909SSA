import random

class CardDeck:  # object
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    # 'self' in python <=> 'this' in C++/Java/C#
    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()


    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit  # tuple
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    # def get_dealer(self):  # getter method
    #     return self._dealer
    #
    # def set_dealer(self, dealer):
    #     pass

    @property
    def dealer(self):  # getter property
        return self._dealer.upper()


    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def bark():
        print("woof! woof!")

    def __len__(self):  # len()
        return len(self._cards)

    def __str__(self):   # str()
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer}, {len(self)})"
