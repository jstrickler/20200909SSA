fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]   # LIST COMPREHENSION
print("f1:", f1, '\n')

# [EXPRESSION for VAR ... in ITERABLE]
# [EXPRESSION for VAR ... in ITERABLE if CONDITION ...]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')


f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

f4 = [len(f) for f in fruits]
print("f4:", f4, '\n')

f5 = [(f, len(f)) for f in fruits if 'a' in f]
print("f5:", f5, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [float(n) * 2 for n in nums]
print("n1:", n1, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last names:", last_names, '\n')

names = [p[:2] for p in people]
print("names:", names, '\n')

last_names_gen = (p[1] for p in people if p[0].startswith('L'))
print(last_names_gen)
for last_name in last_names_gen:
    print(last_name)
print()

fruit_gen = (f.upper() for f in fruits)
print(fruit_gen)
for fruit in fruit_gen:
    print(fruit)
print()

