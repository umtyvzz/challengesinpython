# import random 
# # import my_module
# # print(my_module.pi)
  
# x = random.randint(1, 10)
# print(x)

# y = random.random()
# a = y * 100
# print(a)

print("Welcome to Rock Paper Scissors Game")

import random
ask = int(input("Make your choise ~ 1(Rock) 2(Paper) 3(Scissors)"))
if ask == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
if ask == 2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

if ask == 3:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
x = random.randint(0, 2)

if x == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif x == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
