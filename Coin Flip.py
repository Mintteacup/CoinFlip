import random

flips = 0
heads = 0
tails = 0

flip_count = int(input("How many times do you want to flip the coin? "))

while flips < flip_count:
    flips += 1
    if random.randint(0, 1) == 0 : #0 equals heads and 1 equals tails
        print("Heads")
        heads += 1
    else:
        print("Tails")
        tails += 1
print("Heads amount: " + str(heads))
print("Tails amount: " + str(tails))