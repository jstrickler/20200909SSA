from pprint import pprint
import pandas as pd

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, *_ = line.split(':')
        knight_data[name] = title, color

pprint(knight_data)

print(knight_data['Arthur'][1])
print(knight_data['Robin'][0])
print()

for name, fields in knight_data.items():
    print(fields[0], name)
print()

df = pd.read_table('DATA/knights.txt', sep=":", index_col=0, usecols=[0, 1, 2], names=['name', 'title', 'color'])
print(df)

print(df.loc['Arthur'])


df.to_csv('knights.csv')
df.to_excel('knights.xlsx')

