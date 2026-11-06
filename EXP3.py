#Aim:
Program to demonstrate various string operations.
Algorithm: 
Step 1: Start.
Step 2: Initialize the string.
Step 3: Find and display the length of the string.
Step 4: Convert the string into uppercase and display it.
Step 5: Convert the string into lowercase and display it.
Step 6: Find the character at index and display it.
Step 7: Find the position of character n in the string.
Step 8: Extract a slice from the string and display it.
Step 9: Replace Python with World in the string.
Step 10: Check whether Python is present in the string.
Step 11: Concatenate Hello Python with Programming.
Step 12: Trim/remove unnecessary spaces from the string and display the result.
Step 13: Stop.

#CODE
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 07:56:48 2026

@author: user
"""

s="Hello Python"
print("original string",s)
print("Length:",len(s))
print("Uppercase",s.upper())
print("lowercase",s.lower())
print("Characterstics at index:",s[7])
print("Position of python",s.find("Python"))
print("Slice",s[6:9])
print("Replac:",s.replace("Python","World"))
print(s)
print("Contain Python:","Python" in s)
print("Concatination:",s+"Programming")
s2="  Hello Sumit   "
print("Trim:",s2.strip())


#OUTPUT

original string Hello Python
Length: 12
Uppercase HELLO PYTHON
lowercase hello python
Characterstics at index: y
Position of python 6
Slice Pyt
Replac: Hello World
Hello Python
Contain Python: True
Concatination: Hello PythonProgramming
Trim: Hello Sumit
