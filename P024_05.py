# Team Name: Copiolis
# Team Number: P204
# Problem Number:5

import array
import math
import re
import string
def rep_vowel(string): 
    lowerVowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string: 
        if x in lowerVowels: py
            string = string.replace(x, "*") 
    vowels = ('A', 'E', 'I', 'O', 'U')
    for i in string:
        if i in vowels:
            string = string.replace(i, "&")
    # Print string without vowels 
    print(string) 
  
# Driver program 
a = input()
rep_vowel(a) 