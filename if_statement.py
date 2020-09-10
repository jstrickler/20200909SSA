
value = 62

if value > 75:
    print("kangaroo")
    print("wombat")
elif value > 50:
    print("koala")
    print("platypus")
    if value > 60:
        print("crocodile")
else:
    print("wallaby")
    print("kookaburra")
print("All done")

# x is false if:
# x is numeric, AND equal to 0
# x has a length, and len(x) == 0
# x is None
# x is False

value = "blue"

factor = 12 if value == 'blue' else 35  # ternary operator, like A?B:C

if value == 'blue':
    factor = 12
else:
    factor = 35

# == != > < >= <=

# and or not

#  T and T => T
#  T and F => F
#  F and T => F
#  F and F => F

#  T or T => T
#  T or F => T
#  F or T => T
#  F or F => F

# not T => F
# not F => T

x = 25
y = 15

if (x > 10) and (y < 50):
    print("whoohoo")
