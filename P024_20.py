# HAX 121 2020 Python 3.6.0) Submission Template
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

# Main program:
class Person:

    def __init__(self, ide, height, weight):
        self.height = height
        self.weight = weight
        self.ide = ide

    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight
    def setHeight(self, height):
        self.height = height
    def setWeight(self, weight):
        self.weight = weight

class Student(Person):
    def init(self, ide, height, weight, major):
        self.major = major
        Person.init(self, ide, height, weight)
    def getMajor(self, major):
        return self.major
    def setMajor(self, major):
        self.major = major
# auto input / output
inputs = [input().split() for x in range(5)]
ides = [str(inputs[i][0]) for i in range(5)]
# print(ides)
persons = []
people = ['','','']
for i in range(5):
    persons.append(Student(inputs[i][0], inputs[i][1], inputs[i][2], inputs[i][3]))
# print(persons)
usedIdes = []
for x in range(5):
    people[int(persons[x].ide) - 1] = persons[x]
for x in range(3):
    print(people[x].height, people[x].weight, people[x].major)
print(len(people))

#HENRY YOU HAVE TO MAKE THE PROBLEMS ONLY REGARD INPUT/OUTPUT. REQUIRING STATIC VARIABLES AND PRIVATE VARIABLES CAN DIFFER BETWEEN LANGUAGES. NOTE EVERYTHING IS PYTHON...
    
    
# Using getters and setters example:
# person1 = Person(17, 19)
# person2 = Person(44, 18)
# person3 = Person(50, 20)
# person2.setHeight(20)
# person2.setWeight(40)
# person1.setHeight(30)
# person1.setWeight(35)
# print(person1.height, person1.weight)
# print(person2.height, person2.weight)
# print(person3.height, person3.weight)







