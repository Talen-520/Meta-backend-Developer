#Parent classes vs. child classes
class Employees:
    def __init__(self,name,last)->None:
        self.name = name
        self.last = last

class supervisors(Employees):
    def __init__(self,name,last,password)->None:
        super().__init__(name,last)#the super method has automatically been applied to access the variables there and initialize them within the Supervisors class.
        self.password = password

class chefs(Employees):
    def leave_request(self,days):
        return "May I take a leave for " + str(days) + " days?"

adrian = supervisors("Adrian", "A","apple")
emily =chefs("Emily", "E")
juno = chefs("juno", "J")
print(emily.leave_request(5))
print(adrian.password)
print(emily.name)

# Multiple inheritance
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):#
   pass

c = C()
print(c.a, c.b)

#Multiple inheritance
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a) #2

# issubclass() and isinstance().
print(issubclass(A,B))
print(issubclass(B,A))#“Is B subclass of A?“

class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,B))

#super() function.
#The super() function is a built-in function that can be called inside the derived class
#and gives access to the methods and variables of the parent classes or sibling classes.
# Sibling classes are the classes that share the same parent class. When you call the super() function, you get an object that represents the parent class in return.
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')


a = Fruit("banana")
b = FruitFlavour()