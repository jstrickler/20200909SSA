
list1 = list()  # empty list
colors = ['red', 'purple', 'orange']  # literal list
list2 = []  # empty list
things = 'tractor wombat stethoscope'.split()
print(things)

print(colors, '\n')

colors.append('blue')
colors.append('green')
print(colors, '\n')

# junk = ['fa', 'la', 'la']
# colors.append(junk)
more_colors = ['pink', 'yellow', 'black']

colors.extend(more_colors)
print(colors, '\n')

colors.insert(0, 'teal')
colors.insert(5, 'mauve')
print(colors, '\n')

del colors[5]
print(colors, '\n')

colors.remove('purple')
print(colors, '\n')

c = colors.pop()  # remove and return last element
print(c)
print(colors, '\n')

c = colors.pop(2)
print(c)
print(colors, '\n')

# append()  insert() extend() del remove() pop()

colors[1] = 'scarlet'

print(colors, '\n')

nums = [5, 6, 7]

nums[0] = 12
nums[1] = nums[1] + 1
nums[2] += 1
print(nums, '\n')

print(colors[0], colors[5])
print(nums[0])
print()

print(colors[-1])  # colors[len(colors) - 1]

# print(colors[22]) raises IndexError

print(colors, nums)
print(len(colors), len(nums))

more_colors_again = ['red', 'ocher', 'burnt umber', 'peach', 'navy', 'grey']

colors.extend(more_colors_again)

print(colors, '\n')

# SLICE
#  x[start:stop]  x[start:]  x[:stop]  x[start:stop:step]
#  default start is 0
#  default end is len(x)

print(colors[0:4])  # first 4
print(colors[:4])  # first 4
print(colors[4:7])

# start is INclusive stop is EXclusive

print(colors[8:])  # 8 through end
print(colors[-4:])

#  -4 -3 -2 -1
#  [a, b, c, d]
#   0  1  2  3

actor = "Matt Damon"

print(actor[:4], actor[5:8], actor[-5:], actor[1:3], '\n')

print(colors, '\n')

for color in colors:
    # color = <next value of> colors
    print(color)
print()

s = 'abc'
for char in s:
    print(char)
print()

for color in colors:
    print(color.upper()[:3])
print()

print(len(colors), min(colors), max(colors), sorted(colors), '\n')
print(len(nums), min(nums), max(nums), sorted(nums), sum(nums), '\n')

rcolors = reversed(colors)
print(rcolors, type(rcolors))

for color in rcolors:
    print(color, end=' ')
print('\n\n')

names = ['Fred', 'Mary', 'Srini']
print(nums, names)

combo = zip(names, nums)
print(combo, '\n')

print("round 1:")
for name, number in combo:
    print(name, number)

print("round 2:")
for name, number in combo:
    print(name, number)
print()


for i, color in enumerate(colors):
    print(i, color)
print()

print(list(enumerate(colors)), '\n')

x = [True]
print(x * 10, '\n')

s = 'wombat'
print(s * 5, '\n')
print('-' * 60)

data = [0] * 100
print(data, '\n')

# range(stop)  range(start, stop)  range(start, stop, step)
for i in range(10):
    print(i, end=' ')
print('\n\n')

for i in range(1, 11):
    print(i, end=' ')
print('\n\n')

for i in range(5, 101, 5):
    print(i, end=', ')
print('\n\n')

for i in range(len(colors)):
    print(colors[i])


