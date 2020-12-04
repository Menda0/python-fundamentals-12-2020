
## if then else

name1 = "Robin"
name2 = "Kieran"
name3 = "Robin"

if name1 == name2:
    print("name1 is equal to name2")
else:
    print("name1 not is equal to name2")

if name1 != name2:
    print("name1 not is equal to name2")
else:
    print("name1 is equal to name2")

## Multiple staments

x1 = 2
if x1 == 1:
    print("x1 equals 1")
elif x1 > 2:
    print("x2 is greater than 2")
elif x1 > 1:
    print("x2 is greater than 1")
else:
    print("x1 is something else")

if x1 == 1:
    print("x1 equals 1")
elif x1 >= 2:
    print("x2 is greater than equals 2")
elif x1 > 1:
    print("x2 is greater than 1")
else:
    print("x1 is something else")


## For loop

l1 = [1,2,3,4,5,6,7,8,9,10]

print(l1)

for item in l1:
    print(item, "* 2 =" , item * 2)

## 0 -> 1 * 2 = 2
## 1 -> 2 * 2 = 4
## 2 -> 3 * 2 = 6

for i, item in enumerate(l1):
    print(i, "->", l1[i], "* 2 =", l1[i] * 2)

## 0 -> 1 * 2 = 2
## 1 -> 2 * 2 = 4
## 2 -> 2 * 2 = 4
## 3 -> 2 * 2 = 4

## 0 -> 1 * 2 = 2
## 1 -> 2 * 2 = 4
## 2 -> 3 * 2 = 6

### Pratice 3 ###
# 1. Create list with numbers 1,2,3,4 to 10
# 2. Create another containing the multiples of 2 from 1 to 10
#################

names1 = ["Marco", "George", "Kieran", "Robin"]
names2 = []

for value in names1:
    print(value)

# 0 -> Marco
# 1 -> George
# 2 -> Kieram

for index, value in enumerate(names1):
    print(index)
    print(value)

# 0 -> index = 0 value = Marco
# 1 -> index = 1 value = George
# 2 -> index = 2 value = Kieram

names3 = ["Marco", "George", "Kieran", "Robin"]
ages = [30, 20, 10, 40]

# for index, name in enumerate(name3):
#    print("Name:", name3[index])
#    print("Name:", name)
#    print("Ages", ages[index])


ages2 = [10, 20, 40, 30, 10, 57]
ages3 = []

## Copy every value of age2 to age3
## Add only do age3 the ages bellow 30

people = [
    {
        "name":"Marco",
        "age": 30
    },
    {
        "name": "Kieran",
        "age": 20
    },
    {
        "name": "Robin",
        "age": 10
    },
    {
        "name": "George",
        "age": 40
    }
]
# people_over_30 = []
# people_bellow_30 = []
## Copy every value of people1 to people2
## Copy only the people greater 30 years old to over30 list
## Copy only the people bellow 30 years old to bellow30 list

## Pro tip
people_over_30 = [p for p in people if p["age"] >= 30]
people_bellow_30 = [p for p in people if p["age"] < 30]

print(people_over_30)
print(people_bellow_30)
