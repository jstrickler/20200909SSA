d1 = dict()  # empty dict
state_caps = {'NC': 'Raleigh', 'MD': 'Annapolis', 'VA': 'Richmond', 'WV': 'Charleston'}
d2 = {}

print(state_caps['NC'])
state_caps['PA'] = "Harrisburg"
state_caps['NJ'] = "Trenton"

print(state_caps)
print(state_caps.get('DE'))
print(state_caps.get('DE', "NOT FOUND"))

print(state_caps.setdefault('DE', 'Wilmington'))
print(state_caps)

for state in 'NC', 'NM', 'NY', 'NJ', 'ND', 'NE':
    print(state, state in state_caps)
print()

more_caps = {'TX': 'Austin', 'SC': 'Columbia', 'FL': 'Tallahassee', 'DE': 'Dover'}

state_caps.update(more_caps)
print(state_caps)

del state_caps['TX']

print(state_caps)

print(state_caps.keys())
print(state_caps.values())
print()

for state, capital in state_caps.items():
    print(state, capital)
print()

for state, capital in sorted(state_caps.items()):
    print(state, capital)
print()

print(len(state_caps))




