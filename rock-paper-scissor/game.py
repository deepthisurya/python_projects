import random


def play():
    user = input(
        "Whats your Choice > 'r' for rock 'p' for paper 's' for scissor   --- ")
    
    #Random choice for computer
    computer = random.choice(['r', 'p', 's'])
    # Print the choices
    print("user = "+user+ ", Computer = "+computer)
    if user == computer:
        return 'tie'


    if has_won(user, computer):
        return 'You won'

    return 'You lost'


def has_won(player, opponent):

    # Print the choices
    print("user = "+player+ ", Computer = "+opponent)

    #Winning condition -     r > s , s > p , p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

#The Game Begins
print("Lets play Rock paper Scissors! \n")

#Print the result
print(play())
