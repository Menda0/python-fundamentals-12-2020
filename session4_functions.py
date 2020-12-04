## Simple function without input or output
def func1():
    print("Hello world")


func1()
func1()
func1()


## Simple function with input and ouput
def sausage_maker(pig):
    return "sausages of " + pig


sausage = sausage_maker("Marco")
print(sausage)

print(sausage_maker("Joana"))


## Simple function with input no output
## Create a function with to input x, y
## Print x + y

def print_add(x, y):
    print(x, "+", y, "=", x + y)


print_add(2, 2)
print_add(3, 5)


def add(x, y):
    return x + y


add_2_2 = add(2, 2)
print(add_2_2)


## Create a function the receives(input) of list
## Outputs a list of the values multiplied by two

def multiply_by_2_list(l):
    aux = []

    for value in l:
        aux.append(value * 2)

    return aux


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

out1 = multiply_by_2_list(l1)

print(out1)

l2 = [2, 4, 323, 423, 1, 123, 532]

out2 = multiply_by_2_list(l2)

print(out2)


## Create a function the receives(input) of list
## Outputs a list of the values divide by two



## Create a function with receives an input wich is a dict
## The ouput must be a boolean that checks if the input have a male gender
## True or False
def is_male(person):
    ## out if male or not
    gender = person["gender"]

    if gender == "male":
        return True
    else:
        return False

marco = {
    "name":"Marco",
    "age": 30,
    "gender": "male"
}

is_marco_a_male = is_male(marco)
print("is_marco_a_male:", is_marco_a_male)

sofia = {
    "name":"sofia",
    "age": 10,
    "gender": "female"
}

is_sofia_a_male = is_male(sofia)
print("is_sofia_a_male:", is_sofia_a_male)

## Create a function is_female

## Create a function that checks if a person is older then 30 years old

def is_older_then_30(person):
    return "something"

## Create a function that receives a list and then outputs the numbers divisible by 2
## Number divisible by 2 == (n % 2 == 0)
## input [1,2,3,4,5,6,7,8,9,10]
## output [2,4,8,10]

def numbers_divisible_by_2(l):
    return "something"

## Create a function that retrives male people over 30 years old
## Input is a list of dict
## Output is also list of dict

people = [
    marco,
    sofia,
    {
        "name":"Lucas",
        "age": 40,
        "gender": "male"
    }
]

def get_males_over_30(list_of_people):

    return "list of males over 30"
