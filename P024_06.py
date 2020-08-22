# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P024
# Problem Number: 06

import array
import math
import re
import string

# Class and function definitions:

# Main program:
str = input()
nums = str.split()

for i in range(3):
    nums[i] = int(nums[i])

if (nums[0]**2 + nums[1]**2 == nums[2]**2):
    print(int(0.5 * nums[0] * nums[1]))

else:
    print(0)
