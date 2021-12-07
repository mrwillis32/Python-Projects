class Car:
    def __init__ (self):
        self._protectedVar = 'Ford'

obj = Car()
obj._protectedVar = 'Dodge'
print(obj._protectedVar)





class Canine:
    def __init__(self):# creates a new object in this case is refering to Canine
        self.__privateVar = 'Pitbull'

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar = private

obj = Canine()
obj.getPrivate()    # Get's data from the private value
obj.setPrivate('Blue Heeler')   # This creates a privateVar
obj.getPrivate()






class Parent(object):
    def _protected(self):
        pass

    def __private(self):
        pass

class Child(Parent):
    def foo(self):
        self._protected()

    def bar(self):
        self._Parent__private()


print(foo)
print(bar)
                
