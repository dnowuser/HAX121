# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P204
# Problem Number:10

import array
import math
import re
import string

# Class and function definitions:

# Main program:
x = input()
x = x.lower()
import itertools
for i in x:
    if i == " ":
        x = x.replace(i, "")
x = ''.join(i[0] for i in itertools.groupby(x))
print(x)