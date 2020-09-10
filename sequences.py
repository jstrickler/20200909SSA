#!/usr/bin/python3
from myutils import c2f

# import myutils
# ...myutils.c2f()

ctemps = [-40, 0, 37, 75, 100]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

for c in ctemps:
    print(c, c2f(c))

z = "     Foo    "

print(z.strip().lower())
print(z.lower().strip())


