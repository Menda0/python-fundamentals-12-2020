
## Use animal class
## Super class
class Animal:

    def __init__(self, name, type):
        # print("Animal", name, "of type", type, "was created")

        self.name = name
        self.type = type

    def noise(self):
        return "Animal does not do noise"

    def walks(self):
        return "Animal does not walk"

    def eats(self, food):
        return "Animal does eat food"


## Child class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self, "Dog", "Mammal")

    def walks(self):
        return "Dog start walking"

    def noise(self):
        return "Wof Wof"

    def eats(self, food):
        if food == "steak":
            return "Dog its steak"
        else:
            return "Dog doens't eat " + food

# class Duck:
#
# class Snake:

dog = Dog()

# print(dog.walks())
# print(dog.noise())
# print(dog.eats("steak"))
# print(dog.eats("pasta"))
