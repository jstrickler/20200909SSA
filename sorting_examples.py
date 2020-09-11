
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

f2 = sorted(fruits, key=len)
print("f2:", f2, '\n')

def ignore_case(fruit):
    return fruit.lower()

f3 = sorted(fruits, key=ignore_case)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=str.lower)
print("f4:", f4, '\n')

def custom_sort(elem):
    return len(elem), elem.lower()

f5 = sorted(fruits, key=custom_sort)
print("f5:", f5, '\n')

def wacky(x):
    return x[-1]

f6 = sorted(fruits, key=wacky)
print("f6 (wacky):", f6)
print()

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

for person in sorted(people):
    print(person)
print()

def by_dob(p):
    return p[3]

for person in sorted(people, key=by_dob):
    print(person)
print()

def custom2(person):
    return person[2], person[1]

for person in sorted(people, key=custom2):
    print(person)
print()

for person in sorted(people, key=lambda p: p[3]):
    print(person)
print()

# lambda param, ...: return-value

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for id, name in sorted(airports.items()):
    print(id, name)
print()

for id, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(id, name)
print()

f7 = sorted(fruits, key=str.lower, reverse=True)
print("f7(reversed):", f7, '\n')

fruits.sort(key=str.lower)

print(fruits)


