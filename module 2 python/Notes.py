text = "Hello World" \
            "Hello World" \
            "Hello World" 
print(text)

#time

import time 
start_time = time.time()

#you algorithm here, optimize it

print(round(time.time() - start_time, 2), "seconds")

#enumerate(sequence, start=0)
#iterate through a sequence and keep track of the index of each element
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for x,num in enumerate(num_list):
    print(x,num)
#convert a sequence into a list of tuples.
fruits = ["apple", "banana", "cherry"]

tuples = list(enumerate(fruits))

print(tuples)
#The isinstance() function in Python is a built-in function that checks if an object is an instance of a specified class or type.
#isinstance(object, classinfo)

x = 10

isinstance(x, int) # -> True

a = isinstance("aa",str)
print(a)

#addition resourc: https://docs.python.org/3/tutorial/controlflow.html

#week 2 functions and data structures

# 4 scopes, local, enclosing, global, built-in

#global scope 
my_global = 10

def fn1():
    enclosed = 8
    def fn2():
        local = 5
        print(my_global)
        print(enclosed)
    fn2()
fn1()

#
list1 = [1,2,3,4]
print(list1, sep = " ")

#add to the specific index
list1.insert(len(list1), 5)

#add to the end
list1.append(5)

#add to the end of the list with another list
list1.extend([6,7,8])

#remove  
print(list1.pop(0)) #pop delete by index
#del list1[0] #delete by value
print(list1, sep = " ")

#tuple
#immutable

my_tuple = (1,True,'string','string')
print(type(my_tuple))
print(my_tuple.count('string')) #retun ouccurence of the value
print(my_tuple.index('string')) #return the index of the value first occurence

#set
set_a = {1,2,3,4,4}
print(set_a)

set_a.add(5)
print(f'after number 5 added : {set_a}')
set_a.remove(5) # by value
print(f'after number 5 removed : {set_a}')

set_a.discard(2)
print(f'after number 2 removed : {set_a}')

set_b = {1,2,3,4}
set_c = {4,5,6,7}
print(set_b.union(set_c)) #join two set minus the duplicates
print(set_b | set_c) #same as above
print(set_b.intersection(set_c)) #return the common values
print(set_b & set_c) #same as above
print(set_b.difference(set_c)) #return the difference between two sets
print(set_b - set_c) #same as above
print(set_b.symmetric_difference(set_c)) #return the difference between two sets
print(set_b ^ set_c) #same as above

print(set_b[0]) #error, set is not sequence,doesnt contain order index of all elements inside

#dictionary
#literating with items() values()

my_d ={1:'test','Name':'John','Age':25}

my_d[1] = 'test2' #update value
my_d[2] = 'test3' #add new key value pair
del my_d[1] #delete by key

#literating with items() values()
for key,value in my_d.items():
    print(key,value)
    print(str(key) + " : " + str(value))


#kwargs(keyword args) and args

def sum_of(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(sum_of(1,2,3,4,5,6,7,8,9,10)) # -> 55


def sum_of(**kwargs):
    sum = 0
    for key,value in kwargs.items():
        sum += value
    return sum
print(sum_of(coffee=1.5,tea=2.99,water=3.55,juice=4.99)) #-> 13.03

def sum_of(**kwargs):
    sum = 0
    for i in kwargs.values():
        sum += i
    return sum
print(sum_of(coffee=1,tea=2,water=3,juice=4)) # -> 10

employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"}]
#Example: Employees list
employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id]


print(get_employee_from_dict(12458))

#data structure reference : https://docs.python.org/3/tutorial/datastructures.html
#https://realpython.com/python-data-structures/

#exception handling

def divide_by(a,b):
    return a/b
try:
    ans = divide_by(1,0)

#Exception is the base class for all the exceptions
except ZeroDivisionError as e:
    print('cannot divide by zero')
except Exception as e:
    print('something went wrong',e)
    print(e.__class__)

#file
#read a file
with open('text.txt', 'r') as f:
    data = f.readlines() #['hello world'] return a list of strings
    print(data)
    #or
    #for line in f:
    #    print(line)
    #or read() 
#create a file

with open('new_file.txt','w') as file:
    #file.write('hello world')
    #if I choose to write multiple lines of contents of the file instead of a single line
    file.writelines(['hello world','\n2nd line','\n3rd line'])
#append to the file

try:
    with open('new_file.txt','a') as file:
        file.writelines('\nNew line')
except FileNotFoundError as e:
    print('error', e)


#read a file
#read() -> read the entire file | read(40) -> read the first 40 characters
#readline() -> read first line
#readlines() -> read all the lines and return a list of strings


#absolute path
#/Users/etc/file.py
#or
#C:\Users\Owner\OneDrive\Desktop\Meta Backend\module 2 python\Notes.py

#relative path
#under the same directory
#'somefile.txt'
#'./somefile.txt'

import random
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))#random.choice() returns a random element from a list


#algorithm

#palindrome

def is_palindrome(str):
    return word == word[::-1]


#reserve a string with map and custom function

coffees = ['espresso', 'americano', 'cappuccino', 'latte', 'mocha', 'macchiato', 'affogato']
def reverse(str):
    return str[::-1]
reverse_coffees = map(reverse, coffees)
for x in reverse_coffees:
    print(x)


# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')

# extended slice syntax
#str[start:end:step]

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return str[1:] + str[0]

#map function map(function, iterable), filter(function, iterable)
menu = ["espresso", "americano", "cappuccino", "latte", "mocha", "macchiato", "affogato"]

#return with none, take all object in the list and applies a function
def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee
map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)

#return result with new list only the true values
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)

#encapsulation
class Alpha:
    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 2.  # Private member ‘b’
#self._a is a protected member and can be accessed by the class and its subclasses.

#Private members in Python are conventionally used with preceding double underscores: __. self.__b 
#is a private member of the class Alpha and can only be accessed from within the class Alpha.

#inheritance
class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class

#abstraction
from abc import ABC,   
class ClassName(ABC):
    pass

class myclass:# class  object , Classes mainly perform two kinds of operations, attribute references and instantiation
    a = 5
    print('hello world') 
myc = myclass() #myc is instance object  
print(myclass.a) #5

class Recipe():
    def __new__(cls: type[self]) -> self:
        pass
#The CLS here is not a keyword, but rather a convention.
#It acts as a placeholder for passing the class as its first argument,
#which will be used for creating the new empty object.

#self is a reference to the current instance of the class, and is used to access variables that belongs to the class.
class Recipe():

    def __init__(self,dish,items,time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    def contents(self):
        print("the" + self.dish + "contains" + str(self.items) + "and takes" + str(self.time) + "to cook")
pizza = Recipe("Pizza",["chees","tomato","dough"],30)
pasta = Recipe("Pasta",["chees","bread","tomato"],55)
print(pizza.items)
print(pasta.items)
print(pizza.contents())


# Instantiate a custom Object
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")


#MRO method resolution order

class A:
    num = 5
class B(A):
    num = 9
class C(B):
    pass

print(C.mro()) #-> [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(help(C)) #-> Method resolution order: C, B, A, object


#example 1

class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A): #B  higher precedence
    pass

# Driver code
c = C()
print(c.a())

#example 2
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    #def b(self):
    #    return "Function inside C" -> the function call above would go to A. That is because class C will point to class A as having higher precedence while inheriting.
    pass

class D(C):
    pass

d = D()
print(d.b())

#example 3
class A:
    def c(self):
        return "Function inside A"

class B:
    def c(self):
        return "Function inside B"

class C(A, B):
    def c(self):
        return "Function inside C"

class D(A, C):
    pass

d = D()
print(d.a)
#In this particular case, class D is unable to resolve the order that should be followed, 
# while resolving the value for the variable in cases where the variable is not present in the class of the given object.
#It results in a TypeError because it's unable to create method resolution order (MRO). 
# MRO is Python’s way of resolving the order of precedence of classes while dealing with inheritance.

#resource https://www.python.org/download/releases/2.3/mro/

#access build-in module

#return the value that I get from it in a variable called locations.
import sys
locations = sys.path
print(locations)

for i in locations:
    print(i)

import calendar 
#hover over the function name to see the documentation, ctrl and click
leapdays = calendar.leapdays(2000,2050)
print(leapdays)

print(calendar.isleap(2000))