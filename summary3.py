# data structures : list/dict/set/tuple
# advance looping : comprehensions

# 1) List :Finite, ordered, mutable, sequence of elements

# List Method Reference
my_list = [1,2,3,4,5]

# 1) Extend list by appending elements from the iterable
iterable = [6,7]
my_list.extend(iterable)
print(my_list)
# 2) Insert object before index
index = 1
my_list.insert(index, object)
print(my_list)
# 3) Remove first occurrence of value, or raise ValueError
value = 3
my_list.remove(value)
print(my_list)
# 4) Remove all items
my_list.clear()
print(my_list)
# more methods
# 5) Return number of occurrences of value
my_list.count(value)
print(my_list)
# 6) Return first index of value, or raise ValueError
value = 1
start = 2
stop = 4
my_list.index(value, [start, [stop]])
print(my_list)
# 7) Remove, return item at index (def. last) or IndexError
index = 2
my_list.pop([index])
print(my_list)
# 8) Stable sort *in place*
my_list.sort(key=None, reverse=False)
print(my_list)
# 9) Reverse *in place*.
my_list.reverse()
print(my_list)
# 2) Dictionaries :Mutable map from hashable values to arbitrary objects

# create dictionary
empty = {}
a = dict(one=1, two=2, three=3)
b = {"one": 1, "two": 2, "three": 3}

# Get
print(b['one']) # => 1
print(b.get('one')) # better

# Set
b['two'] = 22 # Modify an existing key
b['four'] = 4 # Add a new key

# delete
del d["one"] #Raises KeyError if invalid key

d.pop("three", default) # => 3 # Remove and return d['three'] or default value if not in the map

d.popitem() # => ("two", 2) #Remove and return an arbitrary (key, value) pair.

# keys, values and items
d = {"one": 1, "two": 2, "three": 3}

print(d.keys())
print(len(d.keys())) # => 3
print(d.items())
print(d.values())
for value in d.values():
    print(value)

# common dictionary operations
# 1)
print(len(d))
# 2)
key = 'one'
if key in d:# equiv. to `key in d.keys()`
    print("True")
# 3)
x = d.copy()
# 4)
d.clear()
# 5)
for key in d: # equiv. to `for key in d.keys():`
    print(key)

# 3) TUPLES : Store collections of heterogeneous data. Think struct- or SQL-like objects. "Freeze" sequence to ensure hashability

# Argument Packing and Unpacking : Comma-separated Rvalues are converted to a tuple
t = 12345, 54321, 'hello!'
print(t) # => (12345, 54321, 'hello!')

x, y, z = t
print(y) # => 54321

# Swapping Values
x,y = 2,5
# better
x,y = y,x
print(x,y)
# or
temp = x
x = y
y = temp
print(x, y)

# fibonaci example
def fib(n):
    """Prints the first n Fibonacci numbers."""
    a, b = 0, 1
    for i in range(n):
        print(i, a)
        a, b = b, a + b

fib(5)

# This also means you should almost never use for i in range(len(sequence)):
# rather use
for index, color in enumerate(['red','green','blue']):
    print(index, color)

# 4) SETS : Unordered collection of distinct hashable elements
# Primary motivation :
# membership testing: O(1) vs. O(n)
# Eliminate duplicate entries
# Easy set operations (intersection, union, etc.)

s = {1, 3, 4}
empty_set = set()
set_from_list = set([1, 2, 1, 4, 3]) # => {1, 3, 4, 2}

basket = {"apple", "orange", "apple", "pear", "banana"}
print(len(basket)) # => 4
print("orange" in basket) # => True

for fruit in basket:
    print(fruit, end='-') # => pear/banana/apple/orange/

# common set operations
a = set("mississippi") # {'i', 'm', 'p', 's'}
# 1) add
a.add('r')
print(a)
# 2) del
a.remove('m') # raises KeyError if 'm' is not present
print(a)
a.discard('x') # same as remove, except no error
print(a)
a.pop() # => 's' (or 'i' or 'p')
print(a)
a.clear()
print(a)
# 3) len
print(len(a)) # => 0

# union , intersection and diff
a = set("abracadabra") # {'a', 'r', 'b', 'c', 'd'}
b = set("alacazam") # {'a', 'm', 'c', 'l', 'z'}
# Set difference
print(a - b) # => {'r', 'd', 'b'}
# Union
print(a | b) # => {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# Intersection
print(a & b) # => {'a', 'c'}
# Symmetric Difference
print(a ^ b) # => {'r', 'd', 'b', 'm', 'z', 'l'}

# example
EFFICIENT_LETTERS = "BCDGIJLMNOPSUVWZ"

def is_efficient(word):
    for letter in word:
        if letter not in EFFICIENT_LETTERS:
            return False
    return True

flag = is_efficient(EFFICIENT_LETTERS)
print(flag)

# looping techniques
# 1) Items in Dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v) # => # gallahad the pure ...

# 2) zip
questions = ['name', 'quest', 'favorite color']
answers = ['Lancelot', 'To seek the holy grail', 'Blue']
for q, a in zip(questions, answers):
    print('What is your {0}? {1}.'.format(q, a))# => # What is your name? Lancelot.

# 3) reversed iteration
for i in reversed(range(1, 10, 2)):
    print(i, end=',') # => # 9, 7, 5, 3, 1,

# 4) sorted
basket = ['pear', 'banana', 'orange', 'pear', 'apple']
for fruit in sorted(basket):
    print(fruit) # => # apple, banana etc...

# Comprehensions
# 1) list comp
new_list = [f(xs) for xs in iter]
# f(xs) = operation
# xs = var
# iter = loop over specified iterable

# predicate condition
new_list2 = [f(xs) for xs in iter if pred(xs)]
# example
setence = 'lionel messi, who currently plays for barca'
word_list = [word.lower() for word in sentence]
word_list_new = [word for word in sentence if len(word) > 3]

# Dictionary Comprehensions
new_dict  = {key_func(vars):val_func(vars) for vars in iterable}
# iterable could be anything not just dict, eg word and len(word) in list
dict_new = {v:k for k, v in d.items()}

# Set Comprehensions
new_set = {func(vars) for vars in iterable}
set_new = {word for word in hamlet if is_palindrome(word.lower()
# Comprehensions as Higher-Level Transformations
# Usually, data structures focus on individual elements.
# Comprehensions represent abstract transformations. Don't say how to build something, just what you want.