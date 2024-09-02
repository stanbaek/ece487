# 🐍 Python Intermediate






### String Formatting
- There are multiple ways to format strings in Python. Here are a few examples:

    ```python
    title = "The legendary pirate captain"
    age = 726.25

    # method 1: (formatted-string)%(values)
    print("%s is %f years old."%(title, age))     # print a string and a floating point
    print("%s is %.4f years old."%(title, age))   # 4 decimal places
    print("%s is %10.4f years old."%(title, age)) # allocate 10 spaces
    print("%s is %d years old."%(title, age))     # print it as integer
    print("%s is %10d years old."%(title, age))   # allocate 10 spaces

    # method 2: (formatted-string).format(values)
    print("{} is {} years old.".format(title, age)) 
    print("{} is {:0.4f} years old.".format(title, age))
    print("{} is {:10.4f} years old.".format(title, age))

    # method 3: f(formatted-string with values)
    print(f"{title} is {age} years old.")
    print(f"{title} is {age:.4f} years old.")
    print(f"{title} is {age:10.4f} years old.")
    ```

    ```
    The legendary pirate captain is 726.250000 years old.
    The legendary pirate captain is 726.2500 years old.
    The legendary pirate captain is   726.2500 years old.
    The legendary pirate captain is 726 years old.
    The legendary pirate captain is        726 years old.
    The legendary pirate captain is 726.25 years old.
    The legendary pirate captain is 726.2500 years old.
    The legendary pirate captain is   726.2500 years old.
    The legendary pirate captain is 726.25 years old.
    The legendary pirate captain is 726.2500 years old.
    The legendary pirate captain is   726.2500 years old.
    ```

### Simplifying Conditional Statements
1. Consider the following `if-elif-else` statement:
    ```Python
    hand = input("What would you like to play? ")
    if hand == "Rock":
        print("It is a valid play.")
    elif hand == "Paper":
        print("It is a valid play.")
    elif hand == "Sciccors":
        print("It is a valid play.")
    else:    
        print("It is an invalid play.")
    ```
1. This code can be simplified by
    ```Python
    hand = input("What would you like to play? ")
    if hand == "Rock" or hand == "Paper" or hand == "Sciccors":
        print("It is a valid play")
    else:    
        print("It is an invalid play")
    ```

3. Further simplified using Python's `in` keyword:
    ```Python
    hand = input("What would you like to play? ")  # This is Pythonic
    if hand in  ("Rock", "Paper", "Scissors"):  
        print("It is a valid play")
    else:    
        print("It is an invalid play")    
    ```
4. The ternary operator is a way of writing conditionals in Python. 

    ```Python
    y = 1

    if y == 1:
        x = 1
    else: 
        x = 0
    print(x)
    ```
1. The code can be simplified by
    ```Python
    x = 1 if y == 1 else 0  # This is Pythonic
    print(x)
    ```






1. You can also use `enumerate()` for more Pythonic code:
    ```Python
    names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne', 'Dr. Baek']
    for index, name in enumerate(names):
        print(index, name)
    ```
1. This will print
    ```
    0 Peter Parker
    1 Clark Kent
    2 Wade Wilson
    3 Bruce Wayne
    4 Dr. Baek
    ```
1. You can start the index from 1:
    ```Python
    names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne', 'Dr. Baek']
    for index, name in enumerate(names, start=1):
        print(index, name)
    ```
1. This will print
    ```
    1 Peter Parker
    2 Clark Kent
    3 Wade Wilson
    4 Bruce Wayne
    5 Dr. Baek
    ```





```Python
# indexing using for loops
index = 0
for name in names:
    print(index, name)
    index += 1
```

It will print
```
0 Peter Parker
1 Clark Kent
2 Wade Wilson
3 Bruce Wayne
4 Dr. Baek
```

```Python
# Pythonic with enumerate
for index, name in enumerate(names):
    print(index, name)
```

It will print
```
0 Peter Parker
1 Clark Kent
2 Wade Wilson
3 Bruce Wayne
4 Dr. Baek
```


```Python
# the index can start with 1 
for index, name in enumerate(names, start=1):
    print(index, name)
```

It will print
```
1 Peter Parker
2 Clark Kent
3 Wade Wilson
4 Bruce Wayne
5 Dr. Baek
```











### Iterating Through Multiple Lists
- You can iterate through multiple lists using `zip()`:



    ```Python
    heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman', 'Pirate Captain']
    for index, name in enumerate(names):
        hero = heroes[index]
        print(f'{name} is actually {hero}')
    ```

It will print
```
Peter Parker is actually Spiderman
Clark Kent is actually Superman
Wade Wilson is actually Deadpool
Bruce Wayne is actually Batman
Dr. Baek is actually Pirate Captain
```


```Python
# Pythonic with zip
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')
```

It will print
```
Peter Parker is actually Spiderman
Clark Kent is actually Superman
Wade Wilson is actually Deadpool
Bruce Wayne is actually Batman
Dr. Baek is actually Pirate Captain
```

```Python
universes = ['Marvel', 'DC', 'Marvel', 'DC', 'USAFA']
for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')
```

It will print
```
Peter Parker is actually Spiderman from Marvel
Clark Kent is actually Superman from DC
Wade Wilson is actually Deadpool from Marvel
Bruce Wayne is actually Batman from DC
Dr. Baek is actually Pirate Captain from USAFA
```

```Python
example_string = "Hello World"
for c in example_string:
    print(c)
```

It will print
```
H
e
l
l
o
 
W
o
r
l
d
```


```Python
animals = list()
# appending to lists in for loop
for value in ['Horse','Mouse','Aardvark']:
    animals.append(value)
    
print(animals)
```

It will print
```
['Horse', 'Mouse', 'Aardvark']
```



```Python
# manipulating lists using for loops
for value in ['a','n','i','m','a','l','s']:
    print(value.upper())
```

It will print
```
A
N
I
M
A
L
S
```


## Deliverables

### Deliverable 1
Write a Python script that computes square roots using the Newton's method of successive approximation, which says that whenever we have a guess $y$ for the value of the square root of a number $x$, we can perform a simple manipulation to get a better guess by averaging $y$ with $x/y$. For example we can compute the square root of 2 as shown below


| Guess    | Quotient          | Average                    |
|:--------:|:-----------------:|:--------------------------:|
| $1$      | $2/1=2$           | $(2+1)/2=1.5$              | 
| $1.5$    | $2/1.5=1.333$     | $(1.333+1.5)/2=1.4176$     |
| $1.4176$ | $2/1.4176=1.4188$ | $(1.4188+1.4176)/2=1.4142$ |                  
| $1.4142$ | $\cdots$          |                            |
| $\vdots$ |                   |                            | 

You need to iterate until $|y^2 - x| < \epsilon$, where $\epsilon = 10^{-9}$ is the tolerance. You are not allowed to use any functions in the `math` module except `math.fabs` for the absolute values.  

### Deliverable 2
Write the `num_vowels` function inside `vowels.py` that takes a string argument and returns the number of lowercase vowels in the string.



























## Purpose
This tutorial will introduce Python data containers, such as lists, tuples, and strings. 

Reference: D. Beazley, Python Essential Reference, 4th ed, Addison Wesley, 2009


<hr>

## Strings

To create string literals, enclose them in single, double, or triple quotes as follows

```python
a = "Hellow World"
b = 'Python is groovy'
c = """Computer says 'No'"""
print(a)
print(b)
print(c)
```

The same type of quote used to start a string must be used to terminate it.  Triple-quoted strings capture all the text that appears prior to the terminating triple quote, as opposed to single- and double-quoted strings, which must be  specified on one logical line.  Triple-quoted strings are useful when the contents of a string literal span multiple lines of text such as the following:

```python
print('''Content-type: text/html

<h1> Hello World </h1>
Click <a href="http://www.python.org">here</a>.
''')
```

Strings are stored as sequences of characters indexed by integers starting at zero

```python
a = "Hello World"
print(a[4])
print(a[:5])
print(a[6:])
print(a[3:8])
```

```python
x = "37"
y = "42"
z = x+y
print(z) # what does this print?  why?
z = int(x)+int(y)
print(z)  # what does this print?
```

## Lists
Lists are sequences of arbitrary objects. You create a list by enclosing values in square brackets, as follows:

```python
names = ["Dave", "Mark", "Ann", "Phil"]
print(names)
```

Lists are indexed by integers, starting with zero. Use the indexing operator to access and modify individual items of the list:

```python
a = names[2]
print(a)
names[0] = "Jeff"
names.append("Paula")
names.insert(2, "Thomas")
print(names)
```

Lists can be sliced:
```Python
x[start:stop:stride]
```

```python
b = names[0:2]
print(b)
c = names[2:]
print(c)
names[1] = 'Jeff'
print(names)
names[0:2] = ['Dave', 'Mark', 'Jeff']
print(names)
```

Use the plus `+` operator to concatenate lists: 

```python
a = [1,2,3]+[4,5,6]
print(a)
```

An empty list can be created bin one of two ways

```python
names = []
print(names)
names = list()
print(names)
```

Lists can contain any kind of Python object, including other lists, as in the following example:

```python
a = [1, "Dave", 3.14, ["Mark", 7, 9, [0, 101]], 10]
```

Items contained in nested lists are accessed by applying more than one indexing operation, as follows:

```python
print(a[1])
print(a[3])
print(a[3][1])
print(a[3][3][1])
```

Objects can be inserted and appended to a list.

```python
# List methods (insert)
list_b.insert(2,'python')
print(list_b)
```

```python
# List methods (append)
list_b.append('.')
print(list_b)
```

## Tuples
To create sinple data structures, you can pack a collection of values together into a single object using a *tuple*. You can create a tuple by enclosing group of values in parentheses like this: 

```python
stock = ("GOOG", 100, 490.10)
address = ('www.python.org', 80)
person = ("Stan", "Baek", "stanley.baek@afacademy")
```

Python often recognizes that a tuple is intended enve if the parentheses are missing

```python
stock = "GOOG", 100, 490.10
address = 'www.python.org', 80
person = "Stan", "Baek", "stanley.baek@afacademy"
```

For completeness, 0- and 1-element tuples can be defined, but have special syntax:

```python
a = ()    # 0-tuple, empty tuple
b = (1,)  # 1-tuple  
c = 1,    # 1-tuple
print(type(a))
print(type(b))
print(type(c))
b = (1)
c = 1
print(type(b))
print(type(c))
```

The values in a tuple can be extracted by numerical index just like a list. However, it is more common to unpack tuples into a set of variables like this

```python
name, shares, price = stock
host, port = address
first_name, last_name, phone = person
```

Although tuples support most of the same operations as lists, such as indexing, slicing, and concatenation, the contents of a utple cannot be modified after creation.  That is, you cannot replace, delete, or append new elements to an exisiting tuple. 

```python
print(stock[1]) 
stock[1] = 200  # error
```

## Dictionaries
- In Python, a dictionary (or dict) is mapping between a set of indices (keys) and a set of values
- The items in a dictionary are key-value pairs
- Keys can be any Python data type
- Dictionaries are unordered

```python
# Dictionaries
eng2sp = {}
eng2sp['one'] = 'uno'
print(eng2sp)
```

```python
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
```

```python
# keys vs values
print(eng2sp.keys())
print(eng2sp.values())
```

