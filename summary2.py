# type redux
# objects , isinstance(4,object) id(object) . python object = suitcase with type and value
# variables : ref to objects , little more than pointer
# named space , symbol table : order local->global->
# variable assignment != copy, instead it adds another reference to the object
# duck typing eg) 1*2 is same as "a" * "2" ?
#  == to check values . is to check type . for None use is rather than == . eg) is for suitcase , == for stuff inside
# escape sequences
# str methods

greeting = "Hello world!"

# 1) slice and index
print(greeting[4]) # => o
# 2) membership
print('world' in greeting) # => True
# 3) lenght of string
print(len(greeting)) # => 13
# 4) returns matchig index
print(greeting.find('lo')) # => 3 (-1 if not found)
# 5) replace
print(greeting.replace('llo', 'y')) # => "hey world!"
# 6) used for searching
print(greeting.startswith('hell')) # => True
# 7) isalpha() , isalphanum() ,
print(greeting.isalpha()) # => False
# 8)lowercase
print(greeting.lower()) # => "hello world! "
# 9) titlecase
print(greeting.title()) # => "Hello World! "
# 10) remove spaces or convert to list?
print(greeting.strip()) # => "Hello world!"
# 11) try rstrip , lstrip aswell
print(greeting.strip('! ')) # => "Hello world" (no '!')

# string <-> list

# a) `split` partitions a string by a delimiter
print('ham cheese bacon'.split()) # => ['ham', 'cheese', 'bacon']
print('03-30-2016'.split(sep='-')) # => ['03', '30', '2016']

# b) `join` creates a string from a list
print(', '.join(['Eric', 'John', 'Michael'])) # => "Eric, John, Michael"

# String Formatting

# Curly braces in strings are placeholders
print('{} {}'.format('monty', 'python')) # => 'monty python'

# Provide values by position or by placeholder
print("{0} can be {1} {0}s".format("strings", "formatted"))
print("{name} loves {food}".format(name="Sam", food="plums"))

# Pure C-style formatting
print("%s, %s, %s. (Act %d)" % ('Words', 'of', 'wisdom', 2)) #=> Words, words, words. (Act 2)

# file io
# f = open(filename,mode) where filename = abs or relative path , mode = r/w/b/a
# f = file oject .
# read 1 f.read(size) 2 f.readline() 3 f.readlines()
# write 1 f.write(string) 2 f.writelines(data) 3 f.flush()

# better use with open() as f:

# scripts, modules , imports
# Run only if called as a script:  if __name__ == '__main__':
# python3.6 -i filename.py

# executable scripts
# chmod +x filename.py
# ./filename.py

# virtual env : Install virtualenv + virtualenvwrapper
