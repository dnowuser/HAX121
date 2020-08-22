# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P024
# Problem Number: 03

import array
import math
import re
import string

# Class and function definitions:

# Main program:
def coprime():
    inp = input()
    inputs=inp.split()
    arr1 = []
    arr2 = []
    for i in range(1,int(inputs[0])+1):
        if int(inputs[0])%i==0:
            arr1.append(i)
    for a in range(1,int(inputs[1])+1):
        if int(inputs[1])%a==0:
            arr2.append(a)
    arr1_as_set = set(arr1)
    intersection = arr1_as_set.intersection(arr2)
    x=list(intersection)
    coprime=True
    if x[-1]==1:
        print(0)
    else:
        print(x[-1])

coprime()