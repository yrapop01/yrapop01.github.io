"""
    Check if a strings contains duplicate letters.
"""

s = input("Enter a string: ")

if len(set(s)) != len(s):
    print("The string contains duplicate letters")
else:
    print("The string does not contain duplicate letters")
