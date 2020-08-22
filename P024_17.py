# Team Name: copiolis
# Team Number: P024
# Problem Number: 17
import array
import math
import re
import string
# Class and function definitions:
def bsearch(arr,l,h,x):
    if h>= l:
        mid= (h+l)// 2
        if arr[mid]== x:
            return 1
        elif arr[mid]> x:
            return 1 + bsearch(arr,l,mid-1,x)
        else:
            return 1 + bsearch(arr,mid+1,h,x)
    else:
        return(-1)
# Main program:

inp=""
while True:
  try:
    inp+=input()
  except Exception as e:
    break

inp = inp.split(" ")
for i in range(0,15):
    inp[i]=int(inp[i])
inp.sort()

biggest =1;
for i in range(0,15):
    isPrime=True
    num=inp[i]
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               isPrime=False
    if(isPrime==True and num>biggest):
        biggest = num

print(bsearch(inp,0,len(inp)-1,biggest))
