# operator and expression in python

You’ll find several categories or groups of operators in Python. Here’s a quick list of those categories:

* Assignment operators  
* Arithmetic operators
* Comparison operators
* Boolean or logical operators
* Identity operators
* Membership operators
* Concatenation and repetition operators
* Bitwise operators

>>> abs(-7)
7
* you call the built-in abs() function to get the absolute value of -7 which is positive

>>> pow(2, 8)
256
* you compute 2 to the power of 8 using the built-in pow() function.

## Assignment operators  
>>> number = 42  number
>>> day = "Friday"  a string, 
>>> digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) tuple,
>>> letters = ["a", "b", "c"]   and list,

## Arithmetic operators
>>> a = 5
>>> b = 2

>>> +a
5
>>> -b
-2
>>> a + b
7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a % b
1
>>> a // b
2
>>> a**b
25

## Comparison operators
### Comparison of Integer Values
>>> a = 10
>>> b = 20
>>> a == b
False
>>> a != b
True
>>> a < b
True
>>> a <= b
True
>>> a > b
False
>>> a >= b
False

>>> x = 30
>>> y = 30
>>> x == y
True
>>> x != y
False
>>> x < y
False
>>> x <= y
True
>>> x > y
False
>>> x >= y
True

### Comparison of Floating-Point Values
>>> x = 1.1 + 2.2
>>> x == 3.3
False

>>> 1.1 + 2.2
3.3000000000000003
#### use this isclose function that compare both operand with the approximate values
>>> from math import isclose

>>> x = 1.1 + 2.2

>>> isclose(x, 3.3)
True

### comparison of string
* You can use the built-in ord() function to learn the Unicode code point of any character in Python.
>>> ord("A")
65
>>> ord("a")
97

>>> "A" == "a"
False
>>> "A" > "a"
False
>>> "A" < "a"
True

>>> "Hello" > "HellO"
True

>>> ord("o")
111
>>> ord("O")
79
### You can also compare strings of different lengths:
>>> "Hello" > "Hello, World!"
False

### Comparison of Lists and tuple
>>> [2, 3] == [2, 3]
True
>>> (2, 3) == (2, 3)
True

>>> [5, 6, 7] < [7, 5, 6]
True
>>> (5, 6, 7) < (7, 5, 6)
True

>>> [4, 3, 2] < [4, 3, 2]
False
>>> (4, 3, 2) < (4, 3, 2)
False

* you can compare base on any length it is, you can compare a lists and tuple with the == and != operator otherwise it will give you an error

## * Boolean or logical operators
>>> number = 42

>>> validation_conditions = (
...     isinstance(number, int),
...     number % 2 == 0,
... )

>>> all(validation_conditions)
True

>>> callable(number)
False
>>> callable(print)
True

## * Identity operators

>>> x = 1001
>>> y = 1001

>>> x == y
True

>>> x is y
False

* You can check an object’s identity using the built-in id() function:
>>> id(x)
4417772080

>>> id(y)
4417766416

>>> a = "Hello, Pythonista!"
>>> b = a

>>> id(a)
4417651936
>>> id(b)
4417651936

>>> a is b
True

>>> x = 1001
>>> y = 1001
>>> x is not y
True

>>> a = "Hello, Pythonista!"
>>> b = a
>>> a is not b
False

## Membership operators

>>> 5 in [2, 3, 5, 9, 7]
True

>>> 8 in [2, 3, 5, 9, 7]
False

>>> 5 not in [2, 3, 5, 9, 7]
False

>>> 8 not in [2, 3, 5, 9, 7]
True

## * Concatenation and repetition operators

>>> "Hello, " + "World!"
'Hello, World!'

>>> ("A", "B", "C") + ("D", "E", "F")
('A', 'B', 'C', 'D', 'E', 'F')

>>> [0, 1, 2, 3] + [4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]

>>> "Hello" * 3
'HelloHelloHello'
>>> 3 * "World!"
'World!World!World!'

>>> ("A", "B", "C") * 3
('A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C')

>>> 3 * [1, 2, 3]
[1, 2, 3, 1, 2, 3, 1, 2, 3]

## Bitwise operators
>>> # Bitwise AND
>>> #   0b1100    12
>>> # & 0b1010    10
>>> # --------
>>> # = 0b1000     8
>>> bin(0b1100 & 0b1010)
'0b1000'
>>> 12 & 10
8

>>> # Bitwise OR
>>> #   0b1100    12
>>> # | 0b1010    10
>>> # --------
>>> # = 0b1110    14
>>> bin(0b1100 | 0b1010)
'0b1110'
>>> 12 | 10
14
