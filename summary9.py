# Python ecosystem
# 1) Python 2 vs 3 vs 3.6? a) The State of Python b) Differences c) Working with Both
# 2) Open Source Philosophy
# 3) Implementations

# 1) Python 2 vs 3

# 1.1) print

# python2
# print is a statement
print "The answer is", 2*2
# Trailing comma suppresses newline
print x,
# Prints a newline
print
# Print to a file object
print >>sys.stderr, "fatal error"
# Print a tuple
print (x, y)

# python3
# print is a function
print("The answer is", 2*2)
# Appends a space instead of a newline
print(x, end=" ")
# You must call the function!
print()
# Print to a file object
print("fatal error", file=sys.stderr)
# Print a tuple
print((x, y))

# 2.1) Views and Iterators instead of Lists

# python2
# .items/keys/values->list
d = {'a': 1, 'b': 2}
d.items() # => [('a', 1), ('b', 2)]
d.iteritems() # => iterator

# map/filter -> list

# range->list, xrange->iterator
range(4) # => [0, 1, 2, 3]
xrange(4) # => iterator
zip([4, 1], 'py') # => list = [(4, 'p'), (1, 'y')]

# python3
# .items/keys/values->view
d = {'a': 1, 'b': 2}
d.items() # => view

# map/filter -> iterator

# range->iterator
range(4) # => iterator

zip([4, 1], 'py') # => iterator

# 3.1) input and raw_input

# python2
# input evaluates user input
>>> x = input('Enter: ')
Enter: 3 + 5
>>> print x, type(x)
8 <type 'int'>
# raw_input returns string
>>> y = raw_input('Enter: ')
Enter: 3 + 5
>>> print y, type(y)
3 + 5 <type 'str'>

# python3
# input returns string
>>> x = input('Enter: ')
Enter: 3 + 5
>>> print x, type(x)
3 + 5 <type 'str'>

# And Many More
# consolidation of integer types
# new-style objects
# integer division
# native unicode support
# exception syntax
# standard library organization and naming
# performance and memory

## Translating Python 2 to Python 3
# Use 2to3 : "reads Python 2.x source code and applies a series of fixers to transform it into valid Python 3.x code"

# Writing Code for Python 2 and Python 3
# 1) Import from __future__ (docs : http://python-future.org/imports.html)
# print_function, division, with_statement, etc.

# 2) Use six : https://pythonhosted.org/six/
# Useful abstractions, but fairly complicated
# Probably only worth it for industry-scale projects

# python at stanford
# COMM 382: Big Data and Causal Inference
# CS 231N: Convolutional Neural Networks for Visual Recognition
# LINGUIST 276: Quantitative Methods in Linguistics
# MS&E 448: Big Financial Data and Algorithmic Trading
# POLISCI 452: Text as Data
# STATS 155: Statistical Methods in Computational Genetics