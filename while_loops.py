i = 0
while i < 3:
    print(i)
    i = i + 1
print()

while True:
    name = input("Enter your name: ")
    if name == 'q':
        break
    if name == '':
        continue

    print(f"Welcome, {name}")
