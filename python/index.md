---
header: Sneaking Like a Python
title: Sneaking Like a Python
---

# Contents

- [Basics](#basics)
- [Topics](#topics)
- [Thanks](#thanks)

# Basics

## Comments

```python
# This is line comment

"""This 
is
multi
line
string, 
which can be used as comment
"""
```

## Dynamic Typing

Python is a *dynamically typed* programming language. Types are decided at runtime. A special built-in function *type* returns the type of an object.

```python
# Run the code below in an interpreter:

s = "Hello, World! שלום"
bt = b'Hello'
n = 55
f = 5.5
b = True
null = None

print(type("Hello"))  # print() is used for putting things on screen
print(type(n))
print(type(f))
print(type(b))
print(type(null))
```

## Unary and Binary Operations

Run the code below in an interpreter and answer the questions below:

```python
# Getting input string from the user
name = input('Your name is ')

# Strings can be added and multiplied
print(name + ", very nice to meet you" + ('!' * 10))
```

<span style="color:red">What happens when two strings are added?</span><br/>
<span style="color:red">What happens when string is multiplied by an integer?</span>

### Arithmetic & Logical Operations

Checking whether <!-- 322.0625 -\frac{(n^3 + 1456)}{16} > m --><math><mrow><mn>322</mn><mi>.</mi><mn>0625</mn><mo>-</mo><mfrac linethickness="1"><mrow><mrow><mo>(</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>1456</mn><mo>)</mo></mrow></mrow><mrow><mrow><mn>16</mn></mrow></mrow></mfrac><mi>></mi><mi>m</mi></mrow></math> for n=12 and m=150:

```python
n = 12
m = 150
322.0625 - (n ** 3) / 16 > m
```

Verifying that 5 < 6 < 8 and that -1 < 0:

```python
(5 < 6 < 8) and (-1 < 0)
```

Verifying that binary number 101 (5) xored with 111 (7) equals 010 (4):

```python
5 ^ 7 == 4
```

Doing the same by manually converting binary strings to integers:

```python
five = int('101', base=2)
seven = int('111', base=2)

n = five ^ seven

print('decimal:', n)

binary = format(n, 'b')

print('binary:', binary)
```

## Lists and Tuples

List is an array in python. Tuple is a list that cannot be changed.

```python
# Declare a list:
lst = [1, 2, 3, 4, 5]

# Change the values of the list:
lst[0] = 'Hello'
lst[-1] = 20
print(lst)
```

<span style="color:red">Why do you see an error when you try to run the code below?</span>

```python
# Declare the following tuple (tuple is a list that cannot be changed)
tpl = (1, 2, 3, 4, 5)

# Set the value of tpl[0] to 0.
tpl[0] = 0
```

What is the complexity of the following operation (assuming the length of lst lst is n):

```python
# in operator checks whether an element is contained in a container:

5 in lst # => True
```

## Indexing

The length of any container (string, list, tuple, etc.) is returned by builtin len() function:

```python
x = [1, 2, 3, 4, 5]
print(len(x))
```

Strings, lists and tuples can all be indexed and iterated. Indexing a container returns new container
of the same type containing elements from the original one. The syntax of indexing a container x is

```python
x[i:j:k]
```

where i, j, k specify the indexes sequence: i, i+k, i+2*k, ..., j. The output container contains
all elements matching the indexes in that sequence in the input container, except the last one.

There are shortcuts that allow avoiding explicit specification of i, j, or k. All the following
boolean expressions True for any non empty container x:

```python
x[i] == x[i:i+1:1]
x[i:j] == x[i:j:1]
x[:j] == x[0:j]
x[:] == x[0:len(x)]
x[-1] == x[-1 + len(x)]
x[::2] == x[0:len(x):2]
x[-1:0:-1] == x[len(x):0:-1]

x = '0123456789'
x[::-1] == x[-1:0:-1] + x[0]
```

<span style="color:red"> In the interpreted print the values of s[0], s[-1], s[0:3], s[-6:], s[::5], s[::-3] for string s defined below:</span>

```python
s = "Rose is a rose is a rose"
```

## Functions

Functions are defined and called as follows:

```python
def function_name(argument):
    print(argument) # notice the identation


function_name(0) # call
```

Sample function which tells if a string is a palindrome:

```python
def is_palindrome(s):
    return s == s[::-1]
```

To test the function above run:

```python
palindrome("abba")
```

## Indentation, Control Flows

As you've noticed in function declaration, indentation is Python’s way of making blocks of statements.
That is, all statements that may be followed by a block of code are terminated by a colon and the following
lines are indented to the right. The block is terminated by a line which moves again to the left.

```python
# If:

if 4 < 6 < 8:
    if 9 < 5:
        print('Jenny')
    print('Jerry')
else:
    print('Lenny')
    
# While:

i = 0
lst = []
while i < 10:
    lst = lst + [i]
    #lst.append(i)
    i += 1

print(lst)
```

<span style="color:red">What would be the output of the code above (run it in the interpreter to verify your answer)?</span>

## Casting

Cast from one type to another can be done using built-in functions int, float, list, tuple, bool, etc.

<span style="color:red">
Print in the interpreter the types and the values of:
- tuple("Anna")
- int(5.5)
- bool([])
- bool([0])
</span>

## Sets and Dictionaries

Sets and dictionaries are implemented in python with hashtables.

```python
# Define a set of strings:
towers = {'Azrieli', 'Electra', 'Time', 'Atrium', 'Sail'}
print(towers)
```

<span style="color:red">What was the complexity of the following expression assuming the set towers contains n elements?</span>

```python
'Electra' in towers
```

# Course Topics

The topics could be changed or corrected according to students' interests, level and progress.

# Thanks

If you enjoyed the course feel free to send gratidute to its author: <a href="https://paypal.me/yrppt">paypal.me/yrppt</a>

<img src="img/python-class.png" alt="python class"/>
