# Topics
# Map and Filter
# Lambdas
# Iterators/Generators
# Decorators

# programming paradigms
# 1) procedural = Sequence of instructions that inform the computer what to do with the program's input
# eg) C
# 2) declarative = Specification describes the problem to be solved, and language implementation figures out the details
# eg) SQL
# 3) object oriented = Deal with collections of objects which maintain internal state and support methods that query or modify this internal state in some way.
# eg) java
# 4) functional = Decomposes into a set of functions, each of which solely takes inputs and produces outputs with no internal
# eg) haskell

# Multi paradigm = Supports several different paradigms, to be combined freely
# eg) C++ , Python

# 1) Functional Programming Concepts
# Primary entity is a "function"
# "Pure" functions are mathematical
# Output depends only on input
# No side effects that modify internal state
# print() and file.write() are side effects

# Why Functional Programming?
# Modularity Encourages small independent functions
# Composability Arrange existing functions for new goals
# Easy Debugging Behavior depends only on input

# common pattern1
def common1(iterable):
    output = []
    for element in iterable:
        val = function(element)
        output.append(val)
    return output
    # or
    # [function(element) for element in iterable]

common1([1,2,3])

# common pattern2
def common2(iterable):
    output = []
    for element in iterable:
        if predicate(element):
            output.append(element)
        return output
        # or
        # [element for element in iterable if predicate(element)]

common2([1,2,3])

# 1) Map / Filter aim : apply some fn(fn not operation) to every element of iterable?
# syntax map(fn, iter)
languages = ["python", "perl", "java", "c++"]
print([len(s) for s in languages]) # >> [6,4,4,3]

map(len, languages)
# does the same thing as [len(s) for s in languages]

# 2) Filter
# syntax filter(pred, iter)
fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34]
print([num for num in fibs if is_even(num)]) # => [2,8,34]

filter(is_even, fibs)
# does the same thing as [num for num in fibs if is_even(num)

# List Comprehensions vs. map + filter

# 1) Memory
# List Comprehensions: buffer all computed results
# Map/Filter: only compute output elements when asked

# 2) Speed
# LCs: no function call overhead, slightly faster usually
# Map/Filter: function calls, faster in some cases

# Lambda Functions = Anonymous, on-the-fly, unnamed functions

# eg) keyword lambda creates an anonymous fn , returns an expression
# syntax: lambda params: expr(params)

# def binds a name to a function object. lambda only creates a function object
# lambda val: val ** 2
# lambda x, y: x * y

# using lambdas
# triple = lambda x: x * 3 # NEVER EVER DO THIS
map(lambda val: val ** 2, range(10)) # Squares from 0**2 to 9**2


# Iterators and Generators = Stream of data,returned one element at a time

# 1) Iterators
# Use iter(data) to build an iterator for a data structure
# Represent finite or infinite data streams
# Use next(iterator) to yield successive values, Raises StopIteration error upon termination

# eg)
# Build an iterator over [1,2,3]
it = iter([1,2,3])

print(next(it)) # => 1
print(next(it)) # => 2
print(next(it)) # => 3
print(next(it)) # raises StopIteration error

# For Loops use Iterators
for data in data_source:
    process(data)
# is really
for data in iter(data_source):
    process(data)

# Builtins use Iterators
# 1) Return a value
# max(iterable)
# min(iterable)
# val in iterable
# val not in iterable
# all(iterable)
# any(iterable)

# 2) Return an iterable
# enumerate(iterable)
# zip(*iterables)
# map(fn, iterable)
# filter(pred, iterable)

# to convert to list use list(iterable) , similary we can use tuple or set

# 2) Generator Expressions = "Lazy List Comprehensions"
# For when you just need a stream of data, not all of it
# eg)
(expensive_function(data) for data in iterable)

# Regular Functions vs. Generator Functions

# Regular Functions Return a single, computed value
# Generators Return an iterator that generates a stream of values

# reg: Each call generates a new private namespace and new local variables,then variables are thrown away
# gen : Local variables aren't thrown away when exiting a function - you can resume where you left off!

# eg) The yield keyword tells Python to convert the function into a generator
def generate_ints(n):
    for i in range(n):
        yield i

g = generate_ints(3)
print(next(g))

# eg) Infinite stream of fibonaci numbers
def generate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

g = generate_fibs()
print(next(g))

# Summary: Why Use Iterators and Generators?
# Compute data on demand
# Reduces in-memory buffering
# Avoid expensive function calls
# Describe (finite or infinite) streams of data
# Asynchronous programming (network/web)
# range, map, filter and others are or use iterables


# Decorators

# 1) Functions as Arguments
# eg)
# map(fn, iterable)
# filter(pred, iterable)

def perform_twice(fn, *args, **kwargs):
    fn(*args, **kwargs)
    fn(*args, **kwargs)

perform_twice(print, 5, 10, sep='&', end='...') # => 5&10...5&10...

# 2) Functions as return values
def make_divisibility_test(n):
    def divisible_by_n(m):
        return m % n == 0
    return divisible_by_n

div_by_3 = make_divisibility_test(3)
filter(div_by_3, range(10)) # generates 0, 3, 6, 9
make_divisibility_test(5)(10) # => True

# 3) both function as argument and return value
# x -> f(x)
# Function as arg -> DECORATOR -> Function as return value
# x'-> g(x')

def debug(function):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return function(*args, **kwargs)
    return wrapper

# eg) find more
def foo(a, b, c=1):
    return (a + b) * c

foo = debug(foo)
foo(2, 3) # prints "Arguments: (2, 3) {} # => returns 5
foo(2, 1, c=3) # prints "Arguments: (2, 1) {'c': 3}" # => returns 9

# using our debug decorator
# @decorator applies a decorator to the following function

@debug
def foo(a, b, c=1):
    return (a + b) * c

foo(5, 3, c=2) # prints "Arguments: (5, 3) {'c': 2}" # => returns 16

# uses of decorators:
# Cache function return value (memoization)
# Set timeout for blocking function
# Mark class properties as readonly
# Mark methods as static methods or class methods
# Handle administrative logic (authorization, routing, etc)

# try
# More map and filter
# Investigate iterators/generators
# Explore function closures
# Build some decorators