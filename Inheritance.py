class Animal:    #Parent Class
    def walk(self):
        print("walk")


class Dog(Animal):  #child1 class
   def bark(self):
       print("bark!!!!!!!!!!!")

class Cat(Animal):  #child2 class
    def meow(self):
        print("meow meow!!")

c1 = Cat()   #objects created for child1 class
c1.walk()
c1.meow()

d1 = Dog()
d1.bark()
