#!/usr/bin/env python

import sys

print(len(sys.argv))

celsius = float(sys.argv[1])

fahrenheit = ((9 * celsius) / 5) + 32

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

