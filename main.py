import os
import time

def clear(): os.system('clear')

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ']
player = 1

########win Flags########
win = 1
draw = -1
running = 0
stop = 1
#########################
game = running
mark ='X'

# This function draws board game
def draw_board():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")

# This Function checks if the position is empty or not
def check_position(x):
    if (board[x] == ' '):
        return True
    else:
        return False

# This FUnction checks player has won or not
def check_win():
    global game
    #Horizontal winning condition
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        game = win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        game = win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        game = win

    # Vertical winning condition
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        game = win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        game = win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        game = win

    #Diagonal Winning condition
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        game = win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        game = win

    # Match tie or Draw condition
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        game = draw

    else:
        game = running

print("Tic-Tac-Toe Game \n Design by MARVIN OKONGO")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait ...")
time.sleep(3)

while(game == running):
    clear()
    draw_board()
    if (player % 2 != 0):
        print("Player 1's turn")
        mark = 'X'
    else:
        print("Player 2's turn")
        mark = 'O'
    choice = int(input("""Enter Position between 1 to 9
    Where you want to mark : """))
    if (check_position(choice)):
        board[choice] = mark
        player += 1
        check_win()

clear()
draw_board()
if (game == draw):
    print('Game Draw')
elif (game == win):
    player -= 1
    if (player % 2 != 0):
        print("Player 1 Wins")
    else:
        print("Player 2 won")