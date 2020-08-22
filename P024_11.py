# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P024
# Problem Number: 11

import array
import math
import re
import string

# Class and function definitions:

# Main program:
arr = input().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

count = 0
for i in range(len(arr) - 1):
    if (arr[i] > arr[i + 1]):
        j = i
        n = arr[i + 1]
        while (j >= 0 and arr[j] > n):
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = n
        count = count + 1

print(count)
