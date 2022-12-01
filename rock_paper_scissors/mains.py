import random

def playing():
    user = input(" 'R' for Rock, 'P' for Paper, 'S' for Scissors")
    com = random.choice(['R','P','S'])

    if user == com:
        return 'tie'
    
    if win(user,com):
        return 'Winner'
    
    
    return 'Lost'
    

def win(player,opponent):
    
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True
    