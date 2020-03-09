---
header: Introduction to Python
title: Introduction to Python
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

print(type("Hello"))
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

<span style="color:red">What happens when two strings are added?</span>
<span style="color:red">What happens when string is multiplied by an integer?</span>

### Arithmetic & Binary Operation

Checking whether $322.0625 -\frac{(n^3 + 1456)} > m$ for $n=12$ and $m = 150$:

```python
n = 12
m = 150
322.0625 - (n ** 3) / 16 > 150
```

Verifying that $5 < 6 < 8$ and that $-1 < 0$:

```python
(5 < 6 < 8) and (-1 < 0)
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
