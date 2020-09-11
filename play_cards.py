
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Melinda")

# d1.shuffle()
# card = d1.draw()
print(d1)  # print(str(d1))
x = str(d1)

d2 = CardDeck("Hank")

print(d1.dealer)
print(type(d1.dealer))

# print(d1.get_dealer())

d1.dealer = "Harry"
print(d1.dealer)

try:
    d1.dealer = 123.45
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards)
for i in range(5):
    print(d1.draw())
print()

print(d1.get_suits())
print(CardDeck.get_suits())

CardDeck.bark()
d1.bark()

j1 = JokerDeck("Jerry")
j1.shuffle()
print(j1, j1.dealer)
for i in range(5):
    print(j1.draw())

print(CardDeck.mro())
print(JokerDeck.mro())

print(j1.cards)
j1.play()

print(len(d1), len(j1))

print(CardDeck.__len__(d1))

print(d1)
print(d2)
