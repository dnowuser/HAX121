# HAX 121 2020 Python 3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P024
# Problem Number: 04

import array
import math
import re
import string

# Class and function definitions:

# Main program:
inputs = []
for i in range(5):
	inputs.append(input().split())
total = 100
operations = []
for i in range(5):
	if inputs[i][0] == "deposit":
		operations.append(float(inputs[i][1]))
	else:
		operations.append(float(inputs[i][1]) * -1)
for i in range(5):
	total += operations[i]
print(round(total))

