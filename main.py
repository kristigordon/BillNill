import random
namesString = input("Give me everyone's names that are at the table and seperate them with a comma.\n")
names = namesString.split(",")
options = len(names)
randomNumber = random.randint(0, options - 1)
personPaying = names[randomNumber]
print(personPaying + " will pay for the meal today!")
