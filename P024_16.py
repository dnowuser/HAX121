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
def isPrime(n) : 

    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False

    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6

    return True

# Main program:
n = int(input())
x = n - 1

while (isPrime(x) == False):
    x = x - 1

print(x)