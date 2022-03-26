import random

guess = int(random.randint(0, 9))
inp = int(input('Enter a number'))
while True:
    if inp == guess:
        print('Guessed')
        break
    else:
        inp = int(input("Wrong Answer!Try again."))
