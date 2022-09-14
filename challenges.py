# Band name generator (dd.mm.yy)(05.06.2022) Day 1
# print("Welcome to band name generator.")
# animal = str(input("what is your favorite animal?: "))
# color = str(input("what is your favorite color?: "))
#
# bandname = f"Your band name is {color} {animal}. Congrats."
#
# print(bandname)

#------------------------------------------------------------------

# Tip calculator (dd.mm.yy)(05.06.2022) Day 2
# print("Welcome to the tip calculator.")
#
# payintotal = float(input("Please enter the bill:"))
# peopleontable = int(input("How many people will split the bill?: "))
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
#
# checkout = payintotal / peopleontable
#
# tip1 = checkout + (checkout * 0.10)
# tip2 = checkout + (checkout * 0.12)
# tip3 = checkout + (checkout * 0.15)
#
# if tip == 10:
#     print(f"You should pay: {tip1}")
# elif tip == 12:
#     print(f"You should pay: {tip2}")
# else:
#     tip == 15
#     print(f"You should pay: {tip3}")

#------------------------------------------------------------------

# Treasure Game (dd.mm.yy)(05.06.2022) Day 3
# print("Welcome to the Treasure Game.")
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')
# print("Welcome to Treasure Game.")
#
# cross = str(input("You're at a cross road. Where do you want to go? Type left or right: "))
#
#
#
# if cross == "left":
#     wait = str(input("You've come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across. "))
#     if wait == "wait":
#         door = str(input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"))
#         if door == "yellow":
#             print("Nicely done my friend. You found it.")
#         elif door == "red":
#             print("Full of fire. Game over.")
#         elif door == "blue":
#             print("It is a room full of beasts you mother fucker.")
#         else:
#             print("There is no room like this GG!")
#     else:
#         print("You were eaten by a Shoal")
# else:
#     print("You chose.... Poorly.")

#------------------------------------------------------------------

# CoinFlipper Game (dd.mm.yy)(05.06.2022)
# print('''
#            __-----__
#       ..;;;--'~~~`--;;;..
#     /;-~IN GOD WE TRUST~-.\
#    //      ,;;;;;;;;      \\
#  .//      ;;;;;    \       \\
#  ||       ;;;;(   /.|       ||
#  ||       ;;;;;;;   _\      ||
#  ||       ';;  ;;;;=        ||
#  ||LIBERTY | ''\;;;;;;      ||
#   \\     ,| '\  '|><| 1995 //
#    \\   |     |      \  A //
#     `;.,|.    |      '\.-'/
#       ~~;;;,._|___.,-;;;~'
#           ''=--'
#           ''')
# print("Welcome to Coinflipper Game!")
#
# import random
#
# random_integer = random.randint(0, 1)
#
# if random_integer == 1:
#     print("The one said Heads won.")
# else:
#     print("The one said Tails won.")

#------------------------------------------------------------------

# Who will pay the bill game. (dd.mm.yy)(06.06.2022)
# print("Welcome to the Who will pay? V1 Game.")
# import random
# given_names = input("Gime me some names seperated by a comma please. ")
# names = given_names.split(", ")
# names1 = random.randint(0, len(names) - 1)
# print(names1)

#------------------------------------------------------------------
# Who will pay the bill game. (dd.mm.yy)(06.06.2022)
# print("Welcome to the Who will pay? V2 Game.")
# print("The check is 888tl")
#
# import random
# enterednames = input("Give me the names will be paying the bill and seperate them by a comma.")
# validnames = enterednames.split(", ")
# who_will_pay = random.choice(validnames)
#
# print(who_will_pay + " will pay the bill. Sorry mate.")

#------------------------------------------------------------------
# New Challenge (dd.mm.yy)(12.09.22)



