def d():
    animal = 'pig'
    def e():
        nonlocal animal
        animal = 'dog'
        print("inside nested function: ",animal)
    print("before calling function: ",animal)
    e()
    print("after calling function: ",animal)
animal = "camel"
d()
print("global animal: ",animal)