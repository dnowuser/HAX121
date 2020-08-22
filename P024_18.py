# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P024
# Problem Number: 01

import array
import math
import re
import string

# Class and function definitions:

# Main program:
arr = input().split()

digits = int(arr[0])
sum = int(arr[1])

num = ""

for i in range(digits):
    if (sum > 9):
        num += "9"
        sum -= 9

    else:
        num += str(sum)
        sum = 0

print(num)