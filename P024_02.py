# Team Name: copiolis
# Team Number: P024
# Problem Number: 02
import array
import math
import re
import string
# Class and function definitions:
# Main program:
inp=input()
fin=""
alph = ["a", "b", "c","d","e","f","g","h","i",
        "j","k","l","m","n","o","p","q","r","s","t",
        "u","v","w","x","y","z"]

for i in range(0, 10):
    old=alph.index(inp[i])
    nextt=((old+3)%26)
    fin+= alph[nextt]

print(fin)
