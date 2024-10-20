
# 🔬 Lab 1 Python

## Deliverable 1: Square Roots

Write a Python script that computes square roots using the Newton's method of successive approximation, which says that whenever we have a guess $y$ for the value of the square root of a number $x$, we can perform a simple manipulation to get a better guess by averaging $y$ with $x/y$. For example we can compute the square root of 3 as shown below

| Guess    | Quotient          | Average                    |
|:--------:|:-----------------:|:--------------------------:|
| $1$      | $3/1=3$           | $(3+1)/2=2.0$              | 
| $2.0$    | $3/2.0=1.5$       | $(2+1.5)/2=1.75$           |
| $1.75$   | $3/1.75=1.7143$   | $(1.75+1.7143)/2=1.7321$   |                  
| $1.7321$ | $\cdots$          |                            |
| $\vdots$ |                   |                            | 


You need to iterate until $|y^2 - x| < \epsilon$, where $\epsilon = 10^{-9}$ is the tolerance. You are not allowed to use any functions in the `math` module except `math.fabs` for the absolute values.  


```python
from math import fabs

# NOTE: DO NOT USE ANY OTHER FUNCTIONS IN THE MATH MODULE


def sqrt(x, guess, tolerance):
    # Write your code here

    # solution
    while fabs(x - guess**2) > tolerance:
        quotient = x / guess
        guess = (quotient + guess) / 2
    return guess
```

Test your function with the following code

```python
numbers = [0.5, 1, 2, 3, 4, 343.23, 1.09**2, 1e-6]
initial_guess = 1
tol = 1e-9

""" This is not Pythonic and slow
for i in range(len(numbers)):
    print(sqrt(numbers[i], initial_guess, tol))
"""

# This is Pythonian and much faster than the code above
for n in numbers:
    print(sqrt(n, initial_guess, tol))
```

## Deliverable 2
Write the `num_vowels` function that takes a string argument and returns the number of lowercase vowels in the string.

```python
def num_vowels(str):
    # write your code here

    # solution
    count = 0
    for c in str:
        count = count + 1 if c in "aieou" else count  # 'aieouAIEOU':

    return count
```

Test your function with the following code

```python
quotes = list()

quotes.append(
    'When the homework is due in an hour, "Do or do not, there is no try."'
)  # 20 vowels
quotes.append(
    'If you think this homework is too convoluted, I would say, "I find your lack of faith disturbing."'
)  # 30 vowels
quotes.append(
    """If you still can't solve this homework, spell "Expecto Patronum!" """
)  # 18 vowels
quotes.append(
    "Don’t worry if it doesn’t work right. If everything did, you’d be out of a job."
)  # 21 vowels
quotes.append(
    "The best thing about a boolean is even if you are wrong, you are only off by a bit."
)  # 28 vowels
quotes.append(
    "There are two ways to write error-free programs; only the third one works. (Alan J. Perlis)"
)  # 25 vowels
quotes.append(
    "One man’s crappy software is another man’s full-time job. (Jessica Gaston)"
)  # 21 vowels
quotes.append("It’s not a bug – it’s an undocumented feature.")  # 15 vowels
quotes.append(
    "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live."
)  # 36 vowels
quotes.append(
    "A good programmer is someone who always looks both ways before crossing a one-way street. (Doug Linder)"
)  # 33 vowels
quotes.append(
    "If debugging is the process of removing software bugs, then programming must be the process of putting them in. (Edsger Dijkstra)"
)  # 34 vowels
quotes.append(
    "In order to understand recursion, one must first understand recursion."
)  # 22 vowels
quotes.append(
    "There are only two kinds of programming languages: those people always bitch about and those nobody uses. (Bjarne Stroustrup)"
)  # 38 vowels
quotes.append(
    "Carefully read comments, but do not always trust them. (Stan Baek)"
)  # 18 vowels

for quote in quotes:
    print(quote + " ==> " + str(num_vowels(quote)) + " vowels.")
```

```python



```
