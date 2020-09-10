from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, *_ = line.split(':')
        knight_data[name] = {
            'title': title,
            'color': color,
            'quest': quest, # , comment
        }

pprint(knight_data)

print(knight_data['Arthur']["color"])
print(knight_data['Robin']["quest"])
print()

for name, fields in knight_data.items():
    print(fields["title"], name)
print()
