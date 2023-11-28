#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number4 = number % 10
if number < 0:
    number1 = number * -1
    number2 = number1 % 10
    number3 = number2 * -1
    if number4 > 5:
        print("Last digit of",
              number, "is", number3, "and is greater than 5")
    elif number4 == 0:
        print("Last digit of", number, "is", number3, "and is 0")
    else:
        print("Last digit of",
              number, "is", number3, "and is less than 6 and not 0")
else:
    if number4 > 5:
        print("Last digit of",
              number, "is", number4, "and is greater than 5")
    elif number4 == 0:
        print("Last digit of", number, "is", number4, "and is 0")
    else:
        print("Last digit of",
              number, "is", number4, "and is less than 6 and not 0")
