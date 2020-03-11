---
header: Python Language Tutorial
title: Python Language Tutorial
---

# Contents

- [Basics](#basics)
- [Classes](#classes)
- [Extras](#extras)
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

For loops can be used to iterate lists and tuples:

```python
# print all values in a list one by one.

for value in lst:
    print(value)
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

While lists, tuples and strings can be indexed only be integer, dictionaries can be index by many different types.

```python
capitals = {'Moscow': 'Russia', 'London':, 'United Kingdom', 'Monaco': 'Monaco'}

print('London is the capital of', capitals['London'])
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

Sets and dictionaries are implemented in python with hashtables. They are defained using curly brackets.

```python
# Define a set of strings:
towers = {'Azrieli', 'Electra', 'Time', 'Atrium', 'Sail'}
print(towers)
```

<span style="color:red">What was the complexity of the following expression assuming the set towers contains n elements?</span>

```python
'Electra' in towers
```

Dictionaries allow assotiating every key element in a set with a value.

```python
# Define a dictionary:
towers = {'Tel Aviv': ['Azrieli', 'Electra'],
          'Ramat Gan': ['Time', 'Atrium'],
          'Haifa': ['Sail']}
print(towers['Tel Aviv'])
```

<span style="color:red">What is the type of towers["Ramat Gan"]? How do you check it in python?</span>

Alternative to create a dictionary:

```python
x = dict(one=1, two=2, three=3)
y = {'one': 1, 'two': 2, 'three': 3}

print(x == y)
```

## Dictionary Arguments

When arguments are passed to a function, they can be past as list (one after another) or as dictionary:

```python
def f(a, b, c):
    print(a, b, c)

f(1, 2, 3)
f(a=1, b=2, c=3)
```

## Default Arguments

When declaring a function, default values can be attached to some arguments -- these arguments
can be ommited when the function is called:

```python
def f(a, b, c=2):
    print(c)

f(1, 1)     # c=2
f(1, 1, 4)  # c=4
```

## Importing Standard Library Functions

Python language has very rich standard library with lots of useful functions. For convinience these functions
are split to different modules. For instance, functions dealing with randomness are put in a module named random.

To use these function the required module must be first imported by its name with import command. For instance,
random module is imported as follows:

```python
import random
```

Then module functions can be called:

```python
n = random.randint(0, 10)
```

The code above puts random integer between 0 and 10 in variable n.

## Standard Input

The module sys contains a variable stdin. It is a special variable that can be used in a for loop:

```python
import sys

for line in sys.stdin:
    print(len(line))
```

the code above prints the length of every line in the standard input.

## Calling Instance Functions

Any variable in python is an object: it is assosiated with a predefined list of functions which get the related
object as their first argument.

To call the assosiated functions of an object, similar syntax to calling functions in a module is used.
For instance, there is a function upper() that is associated with string objects and it makes all letters in a string to be uppercase.

Here is how it can be used:

```python
s = "blue rose"
print(s.upper())  # "BLUE ROSE" should be printed
```

## Strings

Strings can be defined with either double-quote or a single quotes:

```python
"a string" == 'a string'
```

By default, splitting a line in the middle of a string is forbidden. To declare multi-line
string the quote sign is written three times:

```
"""This is a multi
line string"""
````

String containing calculated expressions objects are called f-strings, they must be prefixed with f-letter.
Expressions are surrounded in an f-string with curly braces:

```python
n = 12
s = f"n = {n}"

print(s)
```

## Exercises:

### Exercise 1: Quotes

```python
# define a list of Shakespeare quotes
quotes = ["When we are born, we cry...",
          "My mistress' eyes are nothing like the sun...",
          "There never was a story of more woe...",
          "And the rain it raineth every day..."]
```

Write the following functions:

- `print_quote(i)` that prints quote number i
- `print_quotes(i, j)` which prints quotes from i to j (not including j)
- `print_random_quote()` which prints a random quote
- `choose_and_print_quote()` which lets the user choose a quote and then prints it
- `organazie_quotes()` which asks the user each quote whether it is from play or from a sonnet and returns a dictionary with keys "play" and "sonnet" and with a list of quotes for each key.

### Exercise 2: Reflection

Write a function `remove_non_reflection(d)` which gets a dictionary
and removes all keys that are not reflections of their values. That is,
when the function is written the following expression should be equal to True:

```python
remove_non_reflection({"ab": "ba", "b": "a"}) == {"ab": "ba"}
```

### Exercise 3: Random Password Generator

Write a python file named `password_generator.py` which contains a function named `generate_password(n)`.
The function should return a password of length n (n>2) with the following constrains:

- The password contains only english lowercase and uppercase letters, digits and the signs !@#$%^&*.
- The password must contains at least one uppercase letter and at least one digit.
- Add logic that prints a random password of length 8 when the file is executed and not imported.

Hint: Standard library random module contains random.sample(population, k) function. Look for its description in the internet or with Python's interpreter help function.

### Exercise 4: Echo

Write a program which reads every line from the standard input and prints it to the standard output.

Hint: for string s, there is a function s.strip() which remove any trailing and heading spaces/tabs/newline chars.

# Classes

### Namespaces

Namespace is an association between names and values. For instance, any python dictionary can be seen as a namespace:

```python
{'key1': 'value1', 'key2': 'value2'}
```

Dictionary defined above assosiates names 'key1' and 'key2' with values 'value1' and 'value2' respectively. To get a value
from dictionary we use brackets: d['key'] gets the value associated with name 'key' from dictionary d.

Python modules are also namespaces with completely different indexing syntax: to get a value of a certain name in module we
write module name followed by a dot followed by the required variable name:

```python
import module

value = module.key 
```

### Objects

Another example of a namespace is an object. Like in dictionaries, values to object instances can be added dynamically,
however the syntax for accessing object's values is similar to that of modules:

```python
obj = object()
obj.x = 'new value' # new values can be added dynamically like in dictionaries

print(obj.x) # values are accessed using the dot syntax
```

### Classes

Other kind of namespace is a class. Functions and variables can be bound together by putting them in the same class.
Classes are defined using the class keyword:

```python
class Mazda:
    NAME = 'MAZDA'

    def go(self, source_location, dest_location):
        # self is passed explicitly when instance function is called
        print(f'Going from {source_location} to {dest_location}')

    def print_slogan(self):
        print("Driving matters")

class Honda:
    NAME = 'HONDA'

    def go(self, source_location, dest_location):
        print(f'Going from {source_location} to {dest_location}')


    def print_slogan(self):
        print('The Power of Dreams')

class Ford:
    NAME = 'FORD'

    def go(self, source_location, dest_location):
        print(f'Going from {source_location} to {dest_location}')

    def print_slogan(self):
        print('Everything We Do is Driven By You')
```

To get values from classes we use similar syntax to that of modules and objects:

```python
print(Mazda.NAME)
```

### Instances

A more advanced kind of namespace is an instance. Instance is an object that is also associated with a class. So any
name that was dynamically added to an object and also any name defined in a class can be accessed through an instance.

Instances are created by calling classes as if they were functions.

```python
mazda = Mazda()

mazda.year = 1995 # new values can be added dynamically like in objects
print(mazda.NAME) # class values can be accessed like in classes
```

Notice that in the following example, `brand` instance is associated with different classes during
loop execution, however, the code still works since all of them have a function `print_slogan()`:

```python
brands = [Mazda(), Honda(), Ford()] # list of instances

for brand in brands:
    brand.print_slogan()
```

Therefore, if two objects have the same functions then they can be used interchangeably:

```python
i = int(input(f"Pick a number from 0 to {len(brands)}")
car = brands[i]

car.go('LA', 'NY')
```

### Inheritance and Lookup Order

Classes can be inherited:

```python
class Acura(Honda):
    def print_slogan(self):
        print('The road will never be the same.')

acura = Acura()
acura.print_slogan()
acura.go('A', 'B')
````

The lookup order of a name in an instance is as followed: if the name was added to the instance object
then the assisiated value is returned, otherwise, if that name was defined in the instance class then
the value defined in the class is returned. If the name found niether in an object nor in the class then
it is looked up in all the ancestor classes (the classes from which object class was inherited).

The exact lookup order can be checked using __mro__ variable that is automatically attached to all classes (since python3).

```python
print(Acura.__mro__)
```

### Instance Argument

When a function defined in a class is called from an instances, the instance object itself is automatically passed as first argument.

```python
class C:
    def f(self):
        print(self.key)

c = C()                 # create an instance
c.key = 'object field'  # add a variable to instance object

c.f() # instance argument is passed automatically: `f()` will print "object field"
```

There is a convenrsion to name instance object argument `self`.

### Special Method Names

Class functions are also called methods. There is a family of methods with predefined names that are called special methods.
These methods are used to implement behaviour of built in operations on instances (such as addition, multiplication and others).

For example, `__add__()` method can be used to implement a class whose instances can be added:

```python
class Addable:
    def __add__(self, other):
        result = Addable()
        result.value = self.value + other.value
        return result

x = Addable()
y = Addable()

x.value = 'Hello, '
y.value = 'World!'

z = x + v

print(z.value)
```

<span style="color:red">What does the code above print?</span><br/>

# Extras

# Course Topics

The topics could be changed or corrected according to students' interests, level and progress.

# Thanks

If you enjoyed the course feel free to send gratidute to its author: <a href="https://paypal.me/yrppt">paypal.me/yrppt</a>

<img src="img/python-class.png" alt="python class"/>
