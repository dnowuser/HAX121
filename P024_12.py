# Team Name: copiolis
# Team Number: P024
# Problem Number: 12
import array
import math
import re
import string
# Class and function definitions:
# Main program:
inp = int(input())
count=0
while inp>0:
    if inp-5>=0:
        inp-=5
        count+=1
    elif inp-3>=0:
        inp-=3
        count+=1
    elif inp-1>=0:
        inp-=1
        count+=1

print(count)
