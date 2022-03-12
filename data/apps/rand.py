import random

val_from = input("from: ")
val_to = input("to: ")

if float(val_to) < float(val_from):
    print('the value "to" has to be higher then the value "from"!')
    quit()

val_rand = random.random(float(val_from), float(val_to))
print(val_rand)