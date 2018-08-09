# Advance python
# https://docs.scipy.org/doc/numpy/user/quickstart.html
# https://docs.scipy.org/doc/numpy/user/basics.html
# http://jupyter.org/documentation.html

# Where to Find Interesting Datasets
# Kaggle – hundreds of publicly-accessible datasets for DS
# AWS – public data repositories hosted on AWS
# www.data.gov – >100,000 government datasets
# or... build your own! – log files, APIs, web scraping

# Web app : connect your program to outside world:
# We've seen Flask, Django(, Twisted)
# Assuming cursory background in HTML/CSS/JS
# If not, W3Schools has great tutorials
# Easy to deploy Django/Flask on Heroku/AWS
# Django-on-Heroku or Flask-on-Heroku
# Alternatively, use ngrok to expose local ports to the web

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# "In-Depth Machine Learning Tools"
# 1) Learn Python
# 2) Foundational Machine Learning Skills:
#     Take CS229 or CS221! Or just read the course notes
# 3) Learn the Python Libraries:
    # numpy / scipy / matplotlib / scikit-learn
    # tensorflow / keras for machine intelligence
"In-Depth Machine Learning Tools"
    # Check out CME 193 and CS 20SI at Stanford!
    # https://stanford.edu/~schmit/cme193/
    # http://web.stanford.edu/class/cs20si/

# fun facts
# 'x' in ('x', ) is faster than 'x' == 'x'. Why?
# The Zen of Python is encoded in ROT13
# for loops can have an optional else block
# float('inf') returns a "positive infinity" upper bound
# Python has a small-integer cache for -5 to 256
# The name "Python" refers to Monty Python

# 21 Common Python Style Tricks

# 1) Swap Two Variables
# bad
temp = a
a = b
b = temp
# good
a,b = b,a

# 2)Loop Unpacking
# bad
for bundle in zip([1,2,3],'abc'):
    num, let = bundle
    print(let * num)
for key in d:
    val = d[key]
    print('{}: {}'.format(key,val))
# good
for num, let in zip([1,2,3],'abc'):
    print(let * num)
for key, val in d.items():
    print('{}->{}'.format(key,val))

# 3) Enumerate Iterables
# bad
for index in range(len(arr)):
    elem = arr[index]
    print(elem)
for index in range(len(arr)):
    elem = array[index]
    print(index, elem)
# good
for elem in arr:
    print(elem)
for index, elem in enumerate(arr):
    print(index, elem)

# 4) Joining Strings
# bad
s = ''
for color in colors:
    s += color

s = ''
for color in colors:
    s += color + ', '
s = s[:-2]
# good
s = ''.join(colors)
s = ', '.join(colors)

# 5) Reduce In-Memory Buffering
# bad
', '.join([color.upper() for color in colors])

map(lambda x: int(x) ** 2,[line.strip() for line in file])
sum([n ** 2 for n in range(1000)])
# good
', '.join(color.upper() for color in colors)

map(lambda x: int(x) ** 2, (line.strip() for line in file))
sum(n ** 2 for n in range(1000))

# 6) Chained Comparison Tests
# bad
return 0 < x and x < 10
# good
return 0 < x < 10

# 7) Use in Where Possible
# bad
if d.has_key(key):
    print("Here!")

if x == 1 or x == 2 or x == 3:
    return True

if 'hello'.find('lo') != -1:
    print("Found")
# good
if key in d:
    print("Here!")

if x in [1, 2, 3]:
    return True

if 'lo' in 'hello':
    print("Found")

# 8) Boolean Tests
# bad
if x == True:
    print("Yes")

if len(items) > 0:
    print("Nonempty")

if items != []:
    print("Nonempty")

if x != None:
    print("Something")
# good
if x:
    print("Yes")

if items:
    print("Nonempty")

if items:
    print("Nonempty")

if x is not None:
    print("Something")

# 9) Use _ for ignored variables
# bad
for i in range(10):
    x = input("> ")
    print(x[::-1])
# good
for _ in range(10):
    x = input("> ")
    print(x[::-1])

# 10) Loop Techniques
# bad
for i in range(len(colors)):
    color = colors[i]
    name = names[i]
    print(color, name)

for ind in range(len(elems) - 1,-1, -1):
    print(elems[ind])
# good
for color, name in zip(colors,names):
    print(color, name)

for elem in reversed(elems):
    print(elem)

# 11) Initialize List with Minimum Capacity
# bad
nones = [None, None, None, None]

two_dim = [[None] * 4] * 5]
# good
nones = [None] * 4

two_dim = [[None] * 4 for _ in range(5)]

# 12) Mutable Default Parameters
#  bad
def foo(n, x=[]):
    x.append(n)
    print(x)
foo(1, [4]) # => [4, 1]
foo(3) # => [3]
foo(3) # => [3, 3]
foo(3) # => [3, 3, 3]
# good
def foo(n, x=None):
    if x is None:
        x = []
    x.append(n)
    print(x)
foo(1, [4]) # => [4, 1]
foo(3) # => [3]
foo(3) # => [3, 3]
foo(3) # => [3, 3, 3]

# 13) Format Strings (for now)
# bad
print("Hi %s, you have %i texts" %("Sam", 6))

print("Hi %(name)s, you have %(num)i texts" %{'name':'Sam','num':6})
# good
print("Hi {}, you have {} texts".format("Sam", 6))

print("Hi {name}, you have {num}texts".format(name="Sam", num=6))

# 14) Comprehensions
# bad
out = []
for word in lex:
    if word.endswith('py'):
        out.append(word[:-2])

lengths = set()
for word in lex:
    lengths.add(len(word))
# good
out = [word[:-2] for word in lex if word.endswith('py')]

lengths = {len(word) for word in lex}

# 15) Use collections and itertools
# bad
d = {}
for word in lex:
    if len(word) not in d:
        d[len(word)] = []
    d[len(word)].append(word)
# good
d = collections.defaultdict(list)
for word in lex:
    d[len(word)].append(word)

# 16) Use Context Managers
# bad
f = open('path/to/file')
raw = f.read()
print(1/0)
f.close()

lock = threading.Lock()
lock.acquire()
try:
    print(1/0)
finally:
    lock.release()
# good
with open('path/to/file') as f:
    raw = f.read()
    print(1/0)

with threading.Lock():
    print(1/0)

# 17) EAFP > LBYL
# bad
def safe_div(m, n):
    if n == 0:
        print("Can't divide by 0")
        return None
    return m / n
# good
def safe_div(m, n):
    try:
        return m / n
    except ZeroDivisionError:
        print("Can't divide by 0")
        return None

# 18) Avoid using Catch-Alls
# bad
while True:
    try:
        n = int(input("> "))
    except:
        print("Invalid input.")
    else:
        return n**2
# good
while True:
    try:
        n = int(input("> "))
    except ValueError:
        print("Invalid input.")
    else:
        return n ** 2

# 19) Use Custom Exceptions Abundantly
# bad
if not self.available_cheeses:
    raise ValueError("No cheese!")
# good
class NoCheeseError(ValueError):
    pass

if not self.available_cheeses:
    raise NoCheeseError("I'm afraid we're right out, sir.")

# 20) Magic Methods for Custom Classes
# bad
class Vector():
    def __init__(self, elems):
        self.elems = elems

    def size(self):
        return len(self.elems)

v = Vector([1,2])
len(v) # => fails

# good
class Vector():
    def __init__(self, elems):
        self.elems = elms

    def __len__(self):
        return len(self.elems)

v = Vector([1,2])
len(v) # => succeeds

# 21) Using __name__ for scripts
# bad
def stall():
    time.sleep(10)

stall()
# good
def stall():
    time.sleep(10)

if __name__ == '__main__':
    stall()

# Specific Advice
# Use keyword arguments for optional, tunable parameters
# Utilize functional programming concepts to simplify code
# Employ decorators to factor out administrative logic
# Simplify resource management with context managers

# general advice
# Know all operations on builtin types + common one-liners
# to-do : google common one-liners python
# http://book.pythontips.com/en/latest/one_liners.html
# https://wiki.python.org/moin/Powerful%20Python%20One-Liners
# https://www.quora.com/What-are-some-of-the-most-elegant-greatest-Python-one-liners