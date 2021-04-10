class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f" Hey {self.name}, please speak up!!!")

p1 = Person("Annu")
p1.talk()

p2 = Person("Bharathi")
p2.talk()
