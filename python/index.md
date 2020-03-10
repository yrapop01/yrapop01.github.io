---
header: How To Sneak Like a Python
title: How To Sneak Like a Python
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

print(type("Hello"))  # print function gets comma spereated list of objects and outputs them to the screen.
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

### Arithmetic & Binary Operation

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

# Course Topics

The topics could be changed or corrected according to students' interests, level and progress.

## Part 1

### Basics (half day)

- Running the interpreter
- Basic unary and binary operators, arithmetic and boolean operations
- Lists and tuples
- Indexing
- Casting
- Sets and dictionaries
- Indentation
- Code blocks
- Conditions, loops
- Functions
- Built-in functions
- Strings

### Basic Scripting (half day)

- Exceptions
- Files
- stdin & stdout
- Using modules
- Writing modules
- Using the standard library
- Using random and re modules
- Using subprocess, multiprocessing

### Functions (half day)

- List comprehension
- Dictionary, set and tuple comprehension
- First class functions
- Lambda expressions
- Map, filter and reduce
- Default arguments
- Docstrings

### Generators (half day)

- Closures
- Decorators
- Generators
- Coroutines
- Using next, StopIteration
- Few words about async

### Objects (half day)

- Zen of Python
- Data model
- Built-in objects
- Namespaces
- __dict__, hasattr, getattr
- Dynamic binding
- Classes

### Classes (half day)

- Inheritance
- Special method names
- Private fields
- Multiple inheritance
- Class decorators
- Properties, static methods
- Abstract classes
- Built-in classes
- Typing

## Part 2

### Numpy (half-day)

- Creating numpy arrays
- Basic array manipulations
- Element-wise matrix operations
- Indexing
- Slicing
- Loop elimination
- Changing array types and shapes
- Low level array manipulation

### Jupyter & matplotlib (half day)

- Using jupyter
- Jupyter magic commands
- Timing and debugging in Jupyter
- Using Markdown and Latex in Jupyter
- Showing images in Jupyter
- Using pyplot
- Picking plot colors, setting legends
- Putting multiple figures in one plot
- Pyplot & Jupyter integration
- Annotating plots
- Plot axes

### Pandas (half day)

- Creating Series and DataFrames, reading & writing DataFrames
- Pandas & Jupyter integration
- Built-in operations on strings, numbers, dates
- Applying operations on columns
- Indexing, slicing, adding/removing columns, stacking, deleting rows
- Filtering, sorting, merging
- Extracting basic statistics
- Group by, aggregations
- Using scipy stats & optimizations

### Visualizations (half day)

- Pyplot & pandas integration
- Popular plots: plot, hist, box, bar, area, scatter, pie, density
- Making plots prettier
- Interactive plots
- Using Jupyter widgets

## Part 3

### 1-D Decision Tree (half-day)

- Getting the data (spam/ham email data)
- Splitting the data
- Investigating the data
- Manually vectorizing the data to 1 dimension
- Manually building a simple model
- Visualizing the results
- Building 1-D decision trees

### Adding More Dimensions (half-day)

- Calculating confusion matrices, using scikit metrics
- Adding more dimensions to the decision tree
- Storing data statistics with the model, using pipelines
- One-hot encoding
- Using dict-vectorizer, count-vectorizer, label-encoder
- Scikit-learn and pyplot integration
- Overfitting, underfitting, data leakage, train vs. test error

### Random Forests and Gradient Boosting (half-day)

- Ensemble methods
- Using random forests
- Using AdaBoost
- Gradient Boosting
- Scikit-learn grid search

### Survey (half-day)

- Regression vs Classification
- Naive Bayes
- Nearest Neighbours
- Clustering
- Dimensionality reduction
- K-Means

# Thanks 

If you enjoyed the course feel free to send gratidute to its author: <a href="https://paypal.me/yrppt">paypal.me/yrppt</a>
