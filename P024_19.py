# HAX 121 2020 Python 3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: Copiolis
# Team Number: P024
# Problem Number: 19

import array
import math
import re
import string

# Class and function definitions:

# Main program:
number = int(input())
import math 
factors = []
  
def primeTime(n): 
    while n % 2 == 0: 
        factors.append(2), 
        n = n / 2     
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            factors.append(i), 
            n = n / i 
    if n > 2: 
        factors.append(n) 
primeTime(number) 
factors = sorted(factors, reverse=True)
print(*factors, sep=" ")






