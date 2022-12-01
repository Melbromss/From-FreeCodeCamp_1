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
    
   
    
    def guess_AI():
        low = 1
        high = x
        fb = ''
        while fb != 'c':
            if low != high:
                guess = random.randint(low.high)
            else:
                huess = low # ! also behigh b/c low = high
            fb = input(f'Is {guess} too high, too low (L), or correct (C) ?') 
            if fb =='h':
                high = guess - 1
            elif fb == 'l':
                low = guess + 1
    print("That's right",{guess},"RIGHT !!!!!!")
guess(18)