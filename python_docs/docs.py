# https://docs.python.org/3/tutorial/index.html

# 1) encoding
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2) () can be used for grouping.
# Division (/) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the // operator; to calculate the remainder you can use %:
17 / 3  # classic division returns a float
# >>> 5.666666666666667
17 // 3  # floor division discards the fractional part
# >>> 5
17 % 3  # the % operator returns the remainder of the division
# >>> 2
2 ** 7  # 2 to the power of 7
# >>> 128

# 3) If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

print('C:\some\name')  # here \n means newline!
# >>> C:\some
# ame
print(r'C:\some\name')  # note the r before the quote
# >>> C:\some\name

# 4) Strings can be concatenated (glued together) with the + operator, and repeated with *:
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
# >>> 'unununium'

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
'Py' 'thon'
# >>> 'Python'

# This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
...         'to have them joined together.')
print(text)
# >>>'Put several strings within parentheses to have them joined together.'

# This only works with two literals though, not with variables or expressions:
prefix = 'Py'
prefix + 'thon'  # can't concatenate a variable and a string literal
  ...
SyntaxError: invalid syntax

# If you want to concatenate variables or a variable and a literal, use +:
prefix + 'thon'
# >>> 'Python'

# 5) String Methods : https://docs.python.org/3/library/stdtypes.html#string-methods

# 6) clean the list
letters = ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
# >>> []

# multiple assignment:
a, b = 0, 1

# The print() function writes the value of the argument(s) it is given.
# It differs from just writing the expression you want to write (as we did earlier in the calculator examples) in the way it handles multiple arguments, floating point quantities, and strings.

# 7) better to use enumerate
# To iterate over the indices of a sequence, you can combine range() and len() as follows:
# bad
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
# good
for idx,val in enumerate(a):
    print(idx,val)

# The function list() is another; it creates lists from iterables:
print(list(range(5)))
# >>> [0, 1, 2, 3, 4]

# Coming from other languages, you might object that fib is not a function but a procedure since it doesn’t return a value. In fact, even functions without a return statement do return a value, albeit a rather boring one. This value is called None

# A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an expression), and methodname is the name of a method that is defined by the object’s type.

# def ask_ok(prompt, retries=4)
# default arg ; retries=4
# mandatory arg ; prompt
# optional arg ; retries
# keyword arguments of the form kwarg=value ; retries = 4
# positional arg ; prompt

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch


# 8) Function arguments

# Arbitrary Argument Lists
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
# >>> 'earth/mars/venus'

# Unpacking Argument Lists
# The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:


list(range(3, 6))            # normal call with separate arguments
# >>> [3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
# >>> [3, 4, 5]

# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
# >>> This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

# Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
# >>> 42
f(1)
# >>> 43

# 4.7.7. Function Annotations
# Function annotations are completely optional metadata information about the types used by user-defined functions (see PEP 3107 and PEP 484 for more information).
# Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other part of the function.
# https://www.python.org/dev/peps/pep-3107/
# https://www.python.org/dev/peps/pep-0484/

# Intermezzo: Coding Style
# For Python, PEP 8 the style guide , here are the most important points extracted for you:
# Use 4-space indentation, and no tabs.
# 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.
# Wrap lines so that they don’t exceed 79 characters.
# This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.
# Use blank lines to separate functions and classes, and larger blocks of code inside functions.
# Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
# Name your classes and functions consistently; the convention is to use CamelCase for classes and lower_case_with_underscores for functions and methods. Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).
# Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8, or even plain ASCII work best in any case.

# list methods  : https://docs.python.org/3/tutorial/datastructures.html
# Using Lists as Stacks: where the last element added is the first element retrieved (“last-in, first-out”).
# To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index.
# For example:

stack = [3, 4, 5]
stack.append(6)
# try multiple elements stack.append(6,7,8)
print(stack)
stack.pop()
print(stack)

# Using Lists as Queues
# It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
# >>> 'Eric'
queue.popleft()                 # The second to arrive now leaves
# >>> 'John'
queue                           # Remaining queue in order of arrival
# >>> deque(['Michael', 'Terry', 'Graham'])

# List Comp
# For example, this listcomp combines the elements of two lists if they are not equal:
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# >>> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
vec = [-4, -2, 0, 2, 4]

# 1) create a new list with the values doubled
[x*2 for x in vec]
# >>> [-8, -4, 0, 4, 8]

# 2) filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# >>> [0, 2, 4]

# 3) apply a function to all the elements
[abs(x) for x in vec]
# >>> [4, 2, 0, 2, 4]

# 4) call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# >>> ['banana', 'loganberry', 'passion fruit']

# 5) create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# >>> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# 5.1) the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
# >>> File "<stdin>", line 1, in <module>
#     [x, x**2 for x in range(6)]
#                ^
# SyntaxError: invalid syntax

# 6) flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
# >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Nested List Comprehensions
# Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# The following list comprehension will transpose rows and columns:
[[row[i] for row in matrix] for i in range(4)]
# >>> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:
list(zip(*matrix))
# >>> [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

# dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

# Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead).
# To check whether a single key is in the dictionary, use the in keyword.

tel = {'jack': 4098, 'sape': 4139}
list(tel)
# >>> ['jack', 'guido', 'irv']
sorted(tel)
# >>> ['guido', 'irv', 'jack']

# The comparison operators in and not in check whether a value occurs (does not occur) in a sequence. The operators is and is not compare whether two objects are really the same object; this only matters for mutable objects like lists.
# Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.
# Comparisons may be combined using the Boolean operators and and or, and the outcome of a comparison (or of any other Boolean expression) may be negated with not. These have lower priorities than comparison operators; between them, not has the highest priority and or the lowest, so that A and not B or C is equivalent to (A and (not B)) or C. As always, parentheses can be used to express the desired composition.
# The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false, A and B and C does not evaluate the expression C. When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

# ? if a package’s __init__.py ?

# you can convert any value to a string with the repr() or str() functions.

# Formatted String Literals
# Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# >>>
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678

# The str.rjust() method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left. There are similar methods str.ljust() and str.center(). These methods do not write anything, they just return a new string.

# Old string formatting
print('The value of pi is approximately %5.3f.' %math.pi)

# Methods of File Objects
# 1) f.read(size)
To read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric argument. When size is omitted or negative, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory. Otherwise, at most size bytes are read and returned. If the end of the file has been reached, f.read() will return an empty string ('').

f.read()
# >>> 'This is the entire file.\n'
f.read()
# >>> ''

# 2) f.readline()
# f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.

f.readline()
# >>> 'This is the first line of the file.\n'
f.readline()
# >>> 'Second line of the file\n'
f.readline()
# >>> ''

# 3) f
# For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:

for line in f:
    print(line, end='')

# >>>
# This is the first line of the file.
# Second line of the file

# 4) f.readlines() / list(f)
# If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

# Write
# 1) f.write()
# f.write(string) writes the contents of string to the file, returning the number of characters written.

f.write('This is a test\n')
# >>> 15

# Note
# Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
# >>> 18

# f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
# To change the file object’s position, use f.seek(offset, from_what). The position is computed from adding offset to a reference point; the reference point is selected by the from_what argument. A from_what value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
# >>> 16
f.seek(5)      # Go to the 6th byte in the file
# >>> 5
f.read(1)
# >>> b'5'
f.seek(-3, 2)  # Go to the 3rd byte before the end
# >>> 13
f.read(1)
# >>> b'd'

# When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.
# Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation).
# The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing.
# Reconstructing the data from the string representation is called deserializing.

# 1) json.dumps()
#  If you have an object x, you can view its JSON string representation with a simple line of code:

import json
json.dumps([1, 'simple', 'list'])
# >>> '[1, "simple", "list"]'

# 2) Another variant of the dumps() function, called dump(), simply serializes the object to a text file.
# So if f is a text file object opened for writing, we can do this:
json.dump(x, f)

# 3) To decode the object again, if f is a text file object which has been opened for reading:
x = json.load(f)

# https://docs.python.org/3/library/json.html#module-json
# https://docs.python.org/3/library/pickle.html#module-pickle

# The raise statement allows the programmer to force a specified exception to occur.
# User-defined Exceptions
# Clean-up Actions : finally

# Classes
# Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

# Scopes and Namespaces Example
# This is an example demonstrating how to reference the different scopes and namespaces, and how global and nonlocal affect variable binding:

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# The output of the example code is:
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

# new
# Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok. For example:
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

# Now f, g and h are all attributes of class C that refer to function objects, and consequently they are all methods of instances of C — h being exactly equivalent to g. Note that this practice usually only serves to confuse the reader of a program.

# new
# Methods may call other methods by using method attributes of the self argument:
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

# Private Variables
# “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.
# Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.
# Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:

# Odds and Ends
# Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”, bundling together a few named data items. An empty class definition will do nicely:
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# Operating System Interface
# The os module provides dozens of functions for interacting with the operating system:

# >>> import os
# >>> os.getcwd()      # Return the current working directory
# 'C:\\Python37'
# >>> os.chdir('/server/accesslogs')   # Change current working directory
# >>> os.system('mkdir today')   # Run the command mkdir in the system shell

# For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use:

import shutil
shutil.copyfile('data.db', 'archive.db')
# >>> 'archive.db'
shutil.move('/build/executables', 'installdir')
# >>> 'installdir'

# 10.2. File Wildcards
# The glob module provides a function for making file lists from directory wildcard searches:
import glob
glob.glob('*.py')
# >>> ['primes.py', 'random.py', 'quote.py']

# 10.3. Command Line Arguments
# Common utility scripts often need to process command line arguments. These arguments are stored in the sys module’s argv attribute as a list. For instance the following output results from running python demo.py one two three at the command line:
import sys
print(sys.argv)
# >>> ['demo.py', 'one', 'two', 'three']

# The getopt module processes sys.argv using the conventions of the Unix getopt() function. More powerful and flexible command line processing is provided by the argparse module.

# The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
# >>> 1.6071428571428572
statistics.median(data)
# >>> 1.25
statistics.variance(data)
# >>> 1.3720238095238095

# Internet Access
# There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail:

from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)
# >>> <BR>Nov. 25, 09:43:32 PM EST

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org

... Beware the Ides of March.
... """)
server.quit()

 Dates and Times
The datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation. The module also supports objects that are timezone aware.

>>>
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
10.9. Data Compression
Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.

>>>
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
10.10. Performance Measurement
Some Python users develop a deep interest in knowing the relative performance of different approaches to the same problem. Python provides a measurement tool that answers those questions immediately.

For example, it may be tempting to use the tuple packing and unpacking feature instead of the traditional approach to swapping arguments. The timeit module quickly demonstrates a modest performance advantage:

>>>
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
In contrast to timeit’s fine level of granularity, the profile and pstats modules provide tools for identifying time critical sections in larger blocks of code.

10.11. Quality Control
One approach for developing high quality software is to write tests for each function as it is developed and to run those tests frequently during the development process.

The doctest module provides a tool for scanning a module and validating tests embedded in a program’s docstrings. Test construction is as simple as cutting-and-pasting a typical call along with its results into the docstring. This improves the documentation by providing the user with an example and it allows the doctest module to make sure the code remains true to the documentation:

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
The unittest module is not as effortless as the doctest module, but it allows a more comprehensive set of tests to be maintained in a separate file:

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests

# entire doc ; packages
# https://docs.python.org/3/tutorial/stdlib.html
# date and time
# data compression
# timeit
# quality control
# unit test

# https://docs.python.org/3/tutorial/stdlib2.html
# reprlib / pprint / textwrap locale
# templating : from string import Template
# binary data : import struct
# multi threading : import threading, zipfile
# Logging : import logging
# Weak References
# Tools for working with lists : array , queue, deque , heapq , bisect

# virtual env
# https://docs.python.org/3/tutorial/venv.html
# activate ; deactivate
# install / uninstall package
# freeze requirements.txt , install via requirements.txt
# Pip file?