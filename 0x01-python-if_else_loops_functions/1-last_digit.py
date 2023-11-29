#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)[-1]
n = int(n)

if number < 0:
    print(f"Last digit of {number} is -{last_dig} and is less than 6 and not 0")
elif n < 6 and n != 0:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
elif n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif n > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
else:
    print(f"Last digit of {number} is {n} and is 0")
    
