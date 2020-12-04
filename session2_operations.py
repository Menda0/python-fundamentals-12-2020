

## Number operation
## Add operation

print("1+1=", 1+1)

x1 = 1
x2 = 2

print("x1 + x2 =", x1+x2)

# Minus

print("x1 - x2 =", x1-x2)

# Plus
print("x1 * x2 =", x1 * x2)

# Divide
print("x1 / x2 =", x1 / x2)

# Mod
print("x1 % x2 =", x1 % x2)

# Add and then a plus
print("(x1 + x2) * 2 =", (x1 + x2) * 2)

x3 = x1 + x2

print("x3 =", x3)

## Operations with String

s1 = "Hello"
s2 = "World"

s3 = s1 + " " + s2

print(s3)

## Not suported
## s4 = s1 - s2

## Mixed values operation
## Converting number to string
s4 = s1 + str(x1)

print(s4)

## Convert string to number
s6 = "6"
x5 = int(s6)

print(x5)

## Boolean

have_hair = True
have_mustache = False

i_have_hair_and_mustache = have_hair and have_mustache
i_have_hair_or_mustache = have_hair or have_mustache

print("i_have_hair_and_mustache", i_have_hair_and_mustache)
print("i_have_hair_or_mustache", i_have_hair_or_mustache)

have_i_not_hair = not have_hair
print("have_i_not_hair", have_i_not_hair)

have_i_not_hair_and_mustache = not (have_hair and have_mustache)
print("have_i_not_hair_and_mustache", have_i_not_hair_and_mustache)


## Boolean result operations

## x1 = 1
## x2 = 2

## Less then
b1 = x1 < x2
print("b1 =", b1)

x3 = 3
x4 = 3

b2 = x3 < x4
print("b2 =", b2)

## Lesser then equals
b3 = x3 <= x4
print("b3 =", b2)

## Equals
b4 = x3 == x4

print("b4 =", b4)

name1 = "Robin"
name2 = "Kieran"

b5 = name1 == name2
print("b5 =", b5)

b6 = not b5
print("b6 =", b6)

b7 = name1 != name2
print("b7 =", b7)
