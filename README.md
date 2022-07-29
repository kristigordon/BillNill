# BillNill

This is a program that allows for a group of friends to go out to dinner and have someone be randomly selected to pay the bill by entering each dinner guests name into the program and running a random integer function to select a number that is then mapped to one of the people in the list. 

```
import random
namesString = input("Give me everyone's names that are at the table and seperate them with a comma.\n")
names = namesString.split(",")
options = len(names)
randomNumber = random.randint(0, options - 1)
personPaying = names[randomNumber]
print(personPaying + " will pay for the meal today!")
```

<img width="719" alt="Screen Shot 2022-07-28 at 7 30 54 PM" src="https://user-images.githubusercontent.com/66803124/181653914-b8d2c409-369d-4bd2-9ace-5c4ae1fce48c.png">

