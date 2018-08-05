# Data Structures
# 1) => Lists [items]
# 2) => Dictionaries {key: value}
# 3) => Tuples (frozen, sequence)
# 4) => Sets {unique, hashable, values}
# 5) => Comprehensions [f(xs) for xs in iter]

# Functions
# syntax
def fn_name(param1, param2):
    value = do_something()
    return value
# all functions return something even if the return value is None

# 1) multiple return values
# Sol: use named tuple return value1,value,value3

# 2) return var,data structure , function , object

# Function execution and scope
# First, look in local symbol table
# Next, check symbol tables of enclosing functions (unusual)
# Then, search global (top-level) symbol table
# Finally, check builtin symbols (print, input, etc)
# Order : Function scope -> enclosing function scope -> global scope -> Builtins

# Local Function Scope
x = 2
def foo(y):
    z = 5
    print(locals()) # => prints {'y': 3, 'z': 5}
    print(globals()['x']) # => print 2
    print(x, y, z) # => prints 2, 3, 5
foo(3)

x = 2
def foo(y):
    x = 41
    z = 5
    print(locals()) # prints {'x': 41, 'y': 3, 'z': 5}
    print(globals()['x']) # print 2
    print(x, y, z) # prints 41, 3, 5
foo(3)

# Pass-By-Value or Pass-By-Reference?
# Variables are copied into function's local symbol table.But variables are just references to objects!
# Best to think of it as pass-by-object-reference. Baggage tags in one area can point to suitcases in another

# Parameters
# 1) Default / Named Parameters
# eg) def ask_yn(prompt,retries=4) required paramter = prompt . optional param = retries , defaults to 4

# 2) Keyword Arguments
# eg) def ask_yn(prompt,retries=4) . Here retries is the keyword argument

# order of calling fn with arguments
# eg1)
def ask_yn(prompt, retries=4, complaint='...')
    print("prompt" , prompt)
    print("retries", retries)
    print("complaint", complaint)

# Call with only the mandatory argument
ask_yn('Really quit?')
# Call with one keyword argument
ask_yn('OK to overwrite the file?', retries=2)
# Call with one keyword argument - in any order!
ask_yn('Update status?', complaint='Just Y/N')
# Call with all of the keyword arguments
ask_yn('Send text?', retries=2, complaint='Y/N please!')

# eg2)
def parrot(voltage, state='a stiff', action='voom',type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# 1 positional argument
parrot(1000)
# 1 keyword argument
parrot(voltage=1000)
# 2 keyword arguments
parrot(voltage=1000000, action='VOOOOOM')
# 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)
# 3 positional arguments
parrot('a million', 'bereft of life', 'jump')
# 1 positional, 1 keyword
parrot('a thousand', state='pushing up the daisies')

# invalid calls
parrot() # required argument missing
parrot(voltage=5.0, 'dead') # non-keyword argument after a keyword argument
parrot(110, voltage=220) # duplicate value for the same argument
parrot(actor='John Cleese') # unknown keyword argument

# rules about function calls
# 1) Keyword arguments (x = 4) must follow positional arguments (4)
# 2) All keyword arguments must identify some parameter
# 3) fn(4)-> postional arg -> *args = any no of positional arguments
# 4) fn(x=4)-> keyword arg -> **kwargs = any no of keyword arguments

# Variadic Positional Arguments = any no of positional arguments
# A parameter of form *args captures excess positional args.
# These excess arguments are bundled into an args tuple
# Why? Call functions with any number of positional arguments

# eg) product accepts any number of arguments
def product(*nums,scale=1):
    p = scale
    for n in nums:
        p *= n # p = p*n
    return p

# Suppose we want a product function that works as so:
product(3, 5) # => 15
product(3, 4, 2) # => 24
product(3, 5, scale=10) # => 150
# Note Named parameters after *args are 'keyword-only' arguments (why?) here scale=1 after *nums

# Unpacking Variadic Positional Arguments
# eg)
# Suppose we want to find 2 * 3 * 5 * 7 * ... up to 100
def is_prime(n):
    pass # Some implementation

# Extract all the primes
primes = [number for number in range(2, 100) if is_prime(number)]

print(product(*primes)) # equiv. to product(2, 3, 5, ...)
# The syntax *seq (here *primes) unpacks a sequence into its constituent components

# Variadic Keyword Arguments
# A parameter of the form **kwargs captures all excess keyword arguments.
# These excess arguments are bundled into a kwargs dict
# Why? Allow arbitrary named parameters, usually for configuration.

# eg) quote positional arg , speaker_info var keyword arg

def authorize(quote, **speaker_info):
    print(">", quote)
    print("-" * (len(quote) + 2))
    for k, v in speaker_info.items():
    print(k, v, sep=': ')

authorize("If music be the food of love, play on.",
playwright="Shakespeare",
act=1,
scene=1,
speaker="Duke Orsino"
)

# > If music be the food of love, play on.
# ----------------------------------------
# act: 1
# scene: 1
# speaker: Duke Orsino
# playwright: Shakespeare

# fstr.format(*args, **kwargs)
# All positional arguments go into args. All keyword arguments go into kwargs

print("{0}{b}{1}{a}{0}{2}".format(5, 8, 9, a='z', b='x')) # => 5x8z59
# args = (5, 8, 9)
# kwargs = {'a':'z', 'b':'x'}

# summary eg)
def foo(a, b, c=1, *d, e=1, **f):
    pass

# a,b = Mandatory positional arguments
# c = Optional keyword argument
# *d = Variadic positional argument list - scoops up excess positional args into a tuple
# e = Optional keyword-only argument
# **f = Variadic keyword argument list – scoops up excess keyword args into a dictionary

# Function comments (ref:PEP257)

# The first string literal inside a function body is a docstring
# First line: one-line summary of the function
# Subsequent lines: extended description of function
# Describe parameters (value / expected type) and return
# Many standards have emerged (javadoc, reST, Google)
# The usual rules apply too! List pre-/post-conditions, if any.

def my_function():
    """Summary line: do nothing, but document it.

    Description: No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

# Good practises: PEP8
# Spacing Use 4 spaces to indent. Don't use tabs.
# Use blank lines to separate functions and logical sections inside functions.
# Use spaces around operators and after commas, but not directly inside delimiters eg) a = f(1, 2) + g(3, 4)
# Commenting Comment all nontrivial functions.
# Add header comments at the top of files before any imports.
# If possible, put comments on a line of their own.
# Naming Use snake_case for variables and functions (CamelCase for classes)
# Decomposition and Logic Same as in 106s

# First-Class Functions
def echo(arg): return arg
foo = echo
print(foo)

# To-Do
# What are function objects?
# What can you do with function objects?
# What attributes does a function object possess?
# Can I pass a function as a parameters to other functions?
# Can a function return another function?
# How can I modify a function object?