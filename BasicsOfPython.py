# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 14:11:04 2014

@author: Trost
"""
hello = "Hello"
world = "World"

helloword = hello + world

name = "John"
age = 23
print "%s is %d years old." % (name, age)

a,b = 4,5

print a
print b



#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)


###lists

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print x

### strings

astring = "hello World!"

print len(astring)

print astring.index("o")

print astring.count("l")

print astring[3:7]

print astring.upper()
print astring.lower()

print astring.startswith("hello")
print astring.endswith("nope")

Split = astring.split(" ")
print Split

### booleans

print x == 2

name = "John"
age = 23
if name == "John" and age == 23:
    print "Your name is John, and you are also 23 years old."

if name == "John" or name == "Rick":
    print "Your name is either John or Rick."
    
    
if name in ["John","Rick"]:
    print "your name is either John or Rick."
    
    
### loops
    
primes = [ 2,3,5,7]

for prime in primes:
    print prime
    
    
for x in xrange(2,5): # or range(5)
    print x
    
    
    
for x in xrange(2,8,2): # or range(5)
    print x
    
    
    
count = 0
while count < 5:
    print count
    count += 1  # This is the same as count = count + 1
    
    
    
#break, continue
    
count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in xrange(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print x
    
    
###functions
def my_function():
    print "Allo!"
my_function()


def my_function_with_args(username, greeting):
    print "Hello, %s , From My Function!, I wish you %s"%(username, greeting)
    
my_function_with_args("Thomas","everything")



###Objects
class MyClass:
    variable = "blah"

    def function(self):
        print "This is a message inside the class."
        
        
myobjectx = MyClass()
print myobjectx.variable

myobjectx.variable  = "test"

print myobjectx.variable
myobjectx.function()


### Dictionaries
phonebook = {}
phonebook["john"] = 9231233423423
phonebook["Steve"] = 71389618239462879364
phonebook["Flo"] = 12318626371
 
#can also save strings and numbers combined: phonebook["Stelzer"] = "weird"


for name, number in phonebook.iteritems():
    print "Phone number of %s is %d" % (name, number)
    
phonebook.pop("john")
 #del phonebook["john"]


##modules
import urllib

print dir(urllib) #shows all functions in urllib!

print "\n\n\n"
help(urllib.urlopen)