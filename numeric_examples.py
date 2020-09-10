
i1 = 100
i2 = 0b100  # binary
i3 = 0x100  # hex
i4 = 0o100  # octal
print(i1, i2, i3, i4)

i = 23850293582039852039582039582095820935820395820395820395820395820395820395820935820938502938502938502958

print(i + 1)

f0 = 123.456
f1 = 123.
f2 = .456
f4 = 1.2343e27

print(f0, f1, f2, f4, '\n')

a = 23
b = 9

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)
print()

m = 12
m += 3  # m = m + 3
m *= 4
m /= 3
print(m, '\n')

x = "123   "
y = 456

print(int(x) + y)
print(x + str(y))

x = "DeadBeef"

print(int(x, 16), '\n')

base33_num = '23ghk323enq'
print(int(base33_num, 33))


