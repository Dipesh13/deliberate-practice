# oop

# Objects, Names, Attributes
# An object has identity
# A name is a reference to an object
# A namespace is an associative mapping from names to objects
# An attribute is any name following a dot ('.')

# CLASSES
# Class Objects
# Instance Objects
# Methods vs. Functions

class ClassName:
    <statement>
    <statement>

# Statements are usually assignments or function definitions

# Entering a class definition creates a new "namespace"-ish. Really, a special __dict__ attribute where others live
# Exiting a class definition creates a class object

# Defining a class == creating a class object (like int, str)
# Defining a class != instantiating a class

# Class Objects vs. Instance Objects
# Defining a class creates a class object.Supports 1) attribute reference and 2) instantiation
# Instantiating a class object creates an instance object. Only supports 1) attribute reference

# Class Attribute References

class MyClass:
    """A simple example class"""
    num = 12345
    def greet(self):
        return "Hello world!"

prnt(MyClass.num) # => 12345 (int object)
print(MyClass.greet) # => <function f> (function object)

# Class Instantiation
# Classes are instantiated using parentheses and an optional argument list
x = MyClass(args)

# "Instantiating" a class constructs an instance object of that class object.
# In this case, x is an instance object of the MyClass class object

# Custom Constructor using __init__

class Complex:
    def __init__(self, realpart=0, imagpart=0):
        self.real = realpart
        self.imag = imagpart

# Make an instance object `c`!
c = Complex(3.0, -4.5)
c.real, c.imag # => (3.0, -4.5)

# Class instantiation calls the special method __init__ if it exists
# You can't overload __init__  ,Use keyword arguments or factory methods

# Instance Objects only support attribute reference
# Data attributes = "instance variables" = "data members"

c = Complex(3.0, -4.5)

# Get attributes
c.real, c.imag # => (3.0, -4.5)

# Set attributes
c.real = -9.2
c.imag = 4.1

# Instance Attribute Reference Resolution
class MyOtherClass():
    num = 12345
    def __init__(self):
        self.num = 0

x = MyOtherClass()
print(x.num) # 0 or 12345?
del x.num
print(x.num) # 0 or 12345?

#Attribute references first search the instance's __dict__ attribute, then the class object's

# Setting Data Attributes
# Setting attributes actually inserts into the instance object's __dict__ attribute

# You can set attributes on instance (and class) objects
# on the fly (we used this in the constructor!)
c.counter = 1
while c.counter < 10:
    c.counter = x.counter * 2
    print(c.counter)
del c.counter # Leaves no trace
# prints 1, 2, 4, 8

class MyClass:
    """A simple example class"""
    num = 12345
    def greet(self):
        return "Hello world!"

# Calling Methods
x = MyClass()
x.greet() # => 'Hello world!'
# Weird... doesn't `greet` accept an argument? yes it does, try out

print(type(x.greet)) # => method
print(type(MyClass.greet)) # => function

# Methods vs. Functions
# A method is a function bound to an object.
# method ≈ (object, function)

# Methods calls invoke special semantics
# object.method(arguments) = function(object, arguments)

# eg)
class Pizza:
    def __init__(self, radius, toppings, slices=8):
        self.radius = radius
        self.toppings = toppings
        self.slices_left = slices

    def eat_slice(self):
        if self.slices_left > 0:
            self.slices_left -= 1
        else:
            print("Oh no! Out of pizza")

    def __repr__(self):
        return '{}" pizza'.format(self.radius)

p = Pizza(14, ("Pepperoni", "Olives"), slices=12)
print(Pizza.eat_slice) # => <function Pizza.eat_slice>
print(p.eat_slice) # => <bound method Pizza.eat_slice of 14" Pizza>

method = p.eat_slice
method.__self__ # => 14" Pizza
method.__func__ # => <function Pizza.eat_slice>

p.eat_slice() # Implicitly calls Pizza.eat_slice(p)

# Class and Instance Attributes

# Class Variables VS Instance Variables
class Dog:
    kind = 'Canine' # class variable shared by all instances
    def __init__(self, name):
        self.name = name # instance variable unique to each instance

a = Dog('Astro')
pb = Dog('Mr. Peanut Butter')

a.kind # 'Canine' (shared by all dogs)
pb.kind # 'Canine' (shared by all dogs)
a.name # 'Astro' (unique to a)
pb.name # 'Mr. Peanut Butter' (unique to pb)

# what could go wrong

class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks) # => ['roll over', 'play dead'] (shared value)

# how to solve it?
class Dog:
# Let's try a default argument!
    def __init__(self, name='', tricks=[]):
        self.name = name
        self.tricks = tricks
    def add_trick(self, trick):
       self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks) # => ['roll over', 'play dead'] (shared value)

# solution = New list for each dog
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = [] # New list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks) # => ['roll over']
print(e.tricks) # => ['play dead']

# Privacy
# Nothing is truly private. Clients can modify anything

# Style
# A method's first parameter should always be self. Why? Explicitly differentiate instance and local variables
# Method calls already provide the calling object as the first argument to the class function
# Use verbs for methods and nouns for data attributes
# Attribute names prefixed with a leading underscore are intended to be private (e.g. _spam) (imp)

# Inheritance
# Parentheses indicate inheritance in this case (BaseClassName)
class DerivedClassName(BaseClassName):
    pass

# Facts about Single Inheritance
# A class object 'remembers' its base class
# Python 3 class objects inherit from object (by default)
# Method and attribute lookup begins in the derived class
# Proceeds down the chain of base classes
# Derived methods override (shadow) base methods . Like `virtual` in C++

# Multiple Inheritance
class Derived(Base1, Base2, ..., BaseN):
    """
    Order matters.
    """
    pass

# Attribute Resolution
# Attribute lookup is (almost) depth-first, left-to-right
# Officially, "C3 superclass linearization"
# Class objects have a (hidden) function attribute .mro()
# Shows linearization of base classes

# Attribute Resolution In Action
class A: pass
class B: pass
class C: pass
class D: pass
class E: pass
class K1(A, B, C): pass
class K2(D, B, E): pass
class K3(D, A): pass
class Z(K1, K2, K3): pass

print(Z.mro()) # => [Z, K1, K2, K3, D, A, B, C, E, object]

# Magic Methods
# Python uses __init__ to build classes
# Overriding __init__ lets us hook into the language
# What else can we do? Can we define classes that act like:
# iterators? lists? sets? dictionaries? numbers? comparables?

# Implementing Magic Methods
class MagicClass:
    def __init__(self): pass
    def __contains__(self, key): pass
    def __add__(self, other): pass
    def __iter__(self): pass
    def __next__(self): pass
    def __getitem__(self, key): pass
    def __len__(self): pass
    def __lt__(self, other): pass
    def __eq__(self, other): pass
    def __str__(self): pass
    def __repr__(self): pass # And even more...

x = MagicClass()
y = MagicClass()
print(str(x)) # => x.__str__()
print(x == y) # => x.__eq__(y)
print(x < y) # => x.__lt__(y)
print(x + y) # => x.__add__(y)
print(iter(x)) # => x.__iter__()
print(next(x)) # => x.__next__()
print(len(x)) # => x.__len__()
print(el in x) # => x.__contains__(el)

# http://www.diveintopython3.net/special-method-names.html
# https://docs.python.org/3.4/reference/datamodel.html#specialnames

# eg)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def rotate_90_CC(self):
        self.x, self.y = -self.y, self.x

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "Point({0}, {1})".format(self.x, self.y)

o = Point()
print(o) # => Point(0, 0)
p1 = Point(3, 5)
p2 = Point(4, 6)
print(p1, p2) # => Point(3, 5) Point(4, 6)
p1.rotate_90_CC()
print(p1) # => Point(-5, 3)
print(p1 + p2) # => Point(-1, 9)

# OOP Case Study: Errors and Exceptions

# 1) Syntax errors : errors before execution"
# 2) Exceptions "Errors during execution"

# Handling Exceptions
# eg)
def read_int():
    """Reads an integer from the user (broken)"""
    return int(input("Please enter a number: "))

# what happens if the user enters non numeric input?
# solution
def read_int():
    """Reads an integer from the user (fixed)"""
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops! Invalid input. Try again...")
    return x

# Mechanics of try statement
# 1) Attempt to execute the try clause
# 2a) If no exception occurs, skip the except clause. "Done"
# 2b) If an exception occurs, skip the rest of the try clause.
# 2b i) If the exception's type matches (/ is a subclass of ) that named by except, then execute the except clause. "Done"
# 2b ii) Otherwise, hand off the exception to any outer try statements. If unhandled, 'halt execution'. "Done"

# Conveniences
try:
    distance = int(input("How far? "))
    time = car.speed / distance
    car.drive(time)
except ValueError as e: # Bind a name to the exception instance
    print(e)
except ZeroDivisionError:
    print("Division by zero!")
except (NameError, AttributeError): # Catch multiple exceptions
    print("Bad Car")
except: # "Wildcard" catches everything
    print("Car unexpectedly crashed!")

# good python : raise keyword
try:
    raise NotImplementedError("TODO")
except NotImplementedError:
    print('Looks like an exception to me!')
    raise
# Re-raises the currently active exception

# Good Python: Using else
# syntax
try:
    pass
except ...:
    pass
else:
    do_something() # Code that executes if the try clause does not raise an exception

# Why? Avoid accidentally catching an exception, raised by something other than the code being protected
# eg) database transaction
try:
    update_the_database()
except TransactionError:
    rollback()
    raise
else:
    commit()

# Aside: Python Philosophy
# Don't check if a file exists, then open it. Just try to open it!
# Handle exceptional cases with an except clause (or two)(avoids race conditions too)
# Don't check if a queue is nonempty before popping Just try to pop the element!

# Good Python: Custom Exceptions
class Error(Exception):
    """Base class for errors in this module."""
    pass

class BadLoginError(Error):
    """A user attempted to login with
    an incorrect password."""
    pass

# The finally clause
# executed upon leaving the try except block
try:
    raise NotImplementedError
finally:
    print('Goodbye, world!')

# How finally works
# Always executed before leaving the try statement.
# Unhandled exceptions (not caught, or raised in except) are re-raised after finally executes.
# Also executed "on the way out" (break, continue, return)