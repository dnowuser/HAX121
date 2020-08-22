# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P024
# Problem Number: 08

import array
import math
import re
import string

# Class and function definitions:

# Main program:
arr = input().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort()

print(arr[len(arr) - 1] - arr[0])
