class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hi, I am {}. How it's going on?".format(self.name))


p = Person('Dron')
p.sayHi()

# Person('Dron').sayHi()
