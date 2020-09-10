
counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for line in breakfast_in:
        food = line.rstrip()

        if food not in counts:
            counts[food] = 0

        counts[food] += 1

        # counts[food] = counts[food] + 1

print(counts)
