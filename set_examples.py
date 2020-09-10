
foods1 = ['beans', 'rice', 'tacos', 'tacos', 'tacos', 'tacos', 'lobster', 'nachos', 'samosas', 'dal', 'popcorn']
foods2 = ['popcorn', 'pancakes', 'chicken fricassee', 'nachos', 'rice', 'pineapple']

f1 = set(foods1)
f2 = set(foods2)

print(f1)
print(f2)

print("both:", f1 & f2)
print("only one:", f1 ^ f2)
print("all:", f1 | f2)
print("just f1:", f1 - f2)
print("just f2:", f2 - f1)


food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
print(set(food))

s = set()
s.add('foo')
s.add('bar')
s.add('foo')
print(s)
