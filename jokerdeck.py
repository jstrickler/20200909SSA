
from carddeck import CardDeck

class Game:
    def play(self):
        print("Playing...")

class JokerDeck(CardDeck, Game):

    def _make_deck(self):
        super()._make_deck()
        self._cards.append(('Joker1',))
        self._cards.append(('Joker2',))
