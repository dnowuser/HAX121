# HAX 121 2020 Python 3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P024
# Problem Number: 14

import array
import math
import re
import string

# Class and function definitions:

# Main program:
line1 = input().split()
line2 = input().split()

total = line1 + line2
for i in range(len(total)):
	total[i] = int(total[i])
new = sorted(total)
print(*new, sep = " ")





