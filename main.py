import random

def play():
    user = input("R for rock, P for paper, S for scissor\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It is a tie!.format(computer). You have both chosen{}".format(computer)
    if is_win(user, computer):
        return "You WON!".format(user, computer)
    return "You lost! Computer chose{}".format(user, computer)

def is_win(player, opponent):

    if (player == 'r' and opponent =='s') or (player == 's' and opponent =='p') or (player == 'p' and opponent == 'r'):
        return True
    return False

    if _name_ == '_main_':
        print (play())