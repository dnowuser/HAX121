# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P024
# Problem Number: 15

import array
import math
import re
import string

# Class and function definitions:

# Main program:
n = input()
s = ""
i = len(n) - 1
n = int(n)

while (n > 0):
    s += str(n - (n % (10**i))) + " "
    n = n % (10**i)
    i -= 1

print(s)