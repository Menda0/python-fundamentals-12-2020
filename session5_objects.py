

## Create our first class
## Class is blueprint for our object

class Animal:

    def __init__(self, name, type):
        print("Animal", name, "of type", type, "was created")

        self.name = name
        self.type = type

    ## Check if animal eats that kind of food
    ## if animal eat that kind of food return "Animal eated food"
    ## if not just return "Animal does not eat food"
    ## print(snake.eat("pasta"))  ## Snake does not eat pasta
    ## print(snake.eat("rat"))  ## Snake eats the rat
    def eat(self, food):
        if self.name == "Snake" and food == "rat":
            return "Snake eats this rat"
        elif self.name == "Dog" and food == "stake":
            return "Dog eats this stake"
        elif self.name == "Duck" and food == "bread":
            return "Duck eats this bread"
        else:
            return self.name + " doesn't eat this " + food

    ## Create method that simply print that the animal is walking
    ## Dog starts walking
    ## Snakes does not walk
    def walk(self):
        if self.name == "Snake":
            return self.name + " does not walk"
        elif self.name == "Dog":
            return self.name + " start walking ..."
        elif self.name == "Duck":
            return self.name + " start walking ..."
        else:
            return "Unknown animal"

    def noise(self):

        if self.name == "Snake":
            return "Tssssssssshhh"
        elif self.name == "Dog":
            return "Wof wof"
        elif self.name == "Duck":
            return "Quack Quack"
        else:
            return "No noise"




dog = Animal("Dog", "Mamal")
snake = Animal("Snake", "Reptile")
duck = Animal("Duck", "Bird")

print("Dog says", dog.noise())
print("Snake says", snake.noise())
print("Duck says", duck.noise())


print(dog.walk())
print(snake.walk())
print(duck.walk())


print(snake.eat("pasta")) ## Snake does not eat pasta
print(snake.eat("rat")) ## Snake eated a rat

