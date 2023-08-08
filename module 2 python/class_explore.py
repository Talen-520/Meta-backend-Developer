class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
#a = A(1)
#print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

#   print(a.alpha())
   d = 5
   print(d) #will printed even without instance creation
   # statements inside a class body get executed irrespective of the instance creation. 
   # You will also see how the print statement “Inside class A”, which is inside the constructor, 
   # is not executed because it's inside a function. 

#   print(a)

print("Instantiating B..")
#b = B(a)
#print(a)


#Finally remove all the remaining comments and run the code one more time. 

#Here are a few observations.

#When you try and print the ‘object’ of class A as in lines 21 and 28, you get the address of the object instead of the contents.

#Note how the address of object a is the same both inside class B and in the global scope of the program. It remains the same irrespective of from where it is called.

#The alpha() function is called twice in the program, but you still get the output as 2 every time and not 3. That's because the value is updated only temporarily and not assigned to anything.

#Revise items about classes, function calls and scope in case of confusion.