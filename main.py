import random


def play():
    char = ['r', 'p', 's']
    choice = random.choice(char)
    user = input("Choose rock, paper or scissor: ".lower())
    # incorrect = True
    if user == choice:
        print(f"Comp chose {choice}")
        print("its a tie")

    elif(user == 'r' and choice != 'p') or (user == 's' and choice != 'r') or (user == 'p' and choice != 's'):
        print(f"Comp chose {choice}")
        print('You win!!! ')

    else:
        print(f"Comp chose {choice}")
        print("You lose. BOOOOOOO")


play()

