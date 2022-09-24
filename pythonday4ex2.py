import random

print("Welcome to the game Who is paying?")

# import random

names_string = input("Give me everyone's names, seperated by a comma.")

names = names_string.split(", ")
x = random.randint(0, len(names) - 1)
y = names[x]
print(y)
