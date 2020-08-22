# Team Name: copiolis
# Team Number: P024
# Problem Number: 02
import array
import math
import re
import string
# Class and function definitions:
# Main program:
origStr =""
origArr =[]
finArr=[]
out=""

while True:
  try:
    origStr+=input()
  except Exception as e:
    break

origArr = origStr.split(' ')

for i in range(0,10):
    origArr[i]=int(origArr[i])

finArr = origArr.copy()
finArr.sort();

for i in range(0,10):
    out+=str(finArr.index(origArr[i])) + " "

out.strip
print(out)
