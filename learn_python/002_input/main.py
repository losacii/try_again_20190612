import math

# input string: name
name = input("\nWhat is your name? ")
print("Hi, {}!".format(name))

# convert input to integer
birth_year = input("\nBirth year: ")
age = 2019 - int(birth_year)
print("So you are {} years old now...".format(age))

# calculate
for _ in range(3):
    x = input("\nInput a value: ")
    x = int(x)
    print(x * x)