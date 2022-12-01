import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    
    while guess != random_num:
        guess = input('Choose num between 1 and {x}')
        print(guess)
        if guess < random_num:
            print('Too low, Guess agains!')
        elif guess > random_num:
            print('Too high, Guess agains!')
        elif guess > x:
            print('Out of Range !, agains')
    
    print("That's right")
guess(18)