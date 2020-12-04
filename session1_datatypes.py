## Integer
x = 1
print(x)

## Decimal
x1 = 1.3
print(1.3)

## String
x2 = "This is some text"
print(x2)

## Boolean
x3 = False
x4 = True
print(x3)
print(x4)

# List of integers
# Index start in 0 and goes to lengt of l1 - 1
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l1)
print(l1[0])
print(l1[1])
print(l1[9])

l2 = [1, "hello world", True, 0, 2]

## Calculate length of list
print(len(l2))

## Adding a value to the list
l2.append("Marco Mendao")
print(l2)

## Alter value of the list
l2[0] = 300
print(l2)

## Remove element of list
## Remove by value
l2.remove(300)
print(l2)

# Remove by index
l2.pop(0)
print(l2)

# this is equal to l2.pop(0)
del l2[0]
print(l2)

## Dictionaries
d1 = {
    "name": "Dog",
    "height": 2
}

print(d1["name"])
print(d1["height"])

## Dictionaries with lists
d2 = {
    "name": "Dog",
    "races": ["Pug", "Buldog", "Retriver"]
}

print(d2)
print(d2["name"])
print(d2["races"])
print(d2["races"][1])

## List with Dictionaries
l3 = [d1, d2, {"name":"Cat", "height": 1}]
print(l3)

l4 = [
    {"name": "Peter", "color": "gray"},
    {"name": "Steve", "color": "green"}
]

print(l4[0]["color"])

## Dictionary inside dictionary
d3 = {
    "name": "Wolf Pack",
    "wolves": [
        {"name": "Peter", "color": "gray"},
        {"name": "Steve", "color": "green"}
    ],
    "a":{
        "b": 1,
        "c": 2
    }
}

print(d3["name"])
print(d3["wolves"][0])
print(d3["wolves"][0]["color"])

wolves = d3["wolves"]
print(wolves)

# peter = d3["wolves"][0]
peter = wolves[0]
## peter = {'name': 'Peter', 'color': 'gray'}
print(peter)
peter_color = peter["color"]
print(peter_color)

print(d3["a"]["c"])

a = d3["a"]
c = a["c"]

print(a)
print(c)

### Pratice 1 ###
# 1. Define 3 variables
# 1.1 One variable that contains your name
# 1.2 One variable that will store your age
# 1.3 One variable that stores your job position
# 2. Create dict with the information above
##################
