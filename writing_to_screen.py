
actor = "Chris Hemsworth"

movie = "Thor: Ragnarok"

print(actor, movie)

print(actor, "was in the movie", movie) # no formatting

print("{} was in the movie {}".format(actor, movie))  # python 3 formatting

print(f"{actor} was in the movie {movie}")   # f string (3.6+)

a = 'red'
b = 'purple'
c = 'yellow'

print(a, b, c)
print(a, b, c, sep='')
print(a, b, c, sep='/')
print(a, b, c, sep=' <=> ')

print("one")
print("two")
print("three")
print("one", end=" ")
print("two", end=" ")
print("three")

result = 23.2 / 9.1

print("result is", result)
print("result is {:.2f}".format(result))
print(f"result is {result:.2f}")

value = 23

print("Value: {:04d}".format(value))
print(f"Value: {value:04d}")

print("Value: {:4d}".format(value))
print(f"Value: {value:4d}")

print("Value %4d" % (value))
print("result is %.2f" % (result))
