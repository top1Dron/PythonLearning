class Robot:
    """presents robot with name"""
    # class variable (static variable)
    population = 0

    def __init__(self, name):
        """data initialization"""
        self.name = name
        print("Initialization {}".format(self.name))

        # After creating new robot static variable increments on 1
        Robot.population += 1

    def __del__(self):
        """robot collapses"""
        print("{} collapsed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{0} was the last.".format(self.name))
        else:
            print("We still have {0:d} working robots.".format(Robot.population))

    def sayHi(self):
        """Robot greeting.

        Yes, they can do it."""
        print("Hi. My owners are calling me {}".format(self.name))

    @staticmethod
    def howMany():
        print("We have {} robots".format(Robot.population))


droid1 = Robot("R2-D2")
droid1.sayHi()
Robot.howMany()

droid2 = Robot("C-3PO")
droid2.sayHi()
Robot.howMany()

print("\nRobots can do some work here.\n")

print("Robots finished their work. Let's destroy them.")
del droid1
del droid2

Robot.howMany()
