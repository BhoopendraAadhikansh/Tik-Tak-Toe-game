import random


def display_board(board):
    clear_output()
    print("  "+"|"+"  "+"|")
    print(board[7]+" |"+board[8]+" |"+board[9])
    print("  " + "|" + "  " + "|")
    print("--------")
    print("  "+"|"+"  "+"|")
    print(board[4]+" |"+board[5]+" |"+board[6])
    print("  " + "|" + "  " + "|")
    print("--------")
    print("  "+"|"+"  "+"|")
    print(board[1]+" |"+board[2]+" |"+board[3])
    print("  " + "|" + "  " + "|")
    print("--------")

def player_input():
    markr=" "
    markr = input('Player1: Choose X or O :').upper()

    while markr !="X" and markr !="O":
        markr = input('please choose a correct input X or O: ').upper()
    if markr == "X":
        return ('X', 'O')
    elif markr == 'O':
        return ('O', 'X')

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,marker):
    return ((board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[7] == board[4] == board[1] == marker) or
    (board[2] == board[5] == board[3] == marker) or
    (board[9] == board[6] == board[3] == marker) or
    (board[9] == board[5] == board[1] == marker) or
    (board[1] == board[2] == board[3] == marker) or
    (board[7] == board[5] == board[3] == marker))

def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return'Player1'
    elif flip==1:
        return 'player2'

def space_check(board,position):
    return board[position]==" "
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choise(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('choose a position:(1-9)'))
    return position

def replay():
    choise=input("play again? Enter 'Yes' or 'No'")
    return choise =='Yes'



print('WELCOME TO TIC TAK TOE GAME')
while True:
    the_board=[' ']*10
    Player1_marker,Player2_marker=player_input()
    turn=choose_first()
    print(turn+' will go first')
    play_game=input('Ready to Play? Y or N').upper()
    if play_game == 'Y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn == 'Player1':
            display_board(the_board)
            position=player_choise(the_board)
            place_marker(the_board,Player1_marker,position)

            if win_check(the_board,Player1_marker):
                display_board(the_board)
                print('Player1 has WON!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE game')
                    break
                else:
                    turn='Player2'
        else:
            display_board(the_board)
            position=player_choise(the_board)
            place_marker(the_board,Player2_marker,position)
            if win_check(the_board,Player2_marker):
                display_board(the_board)
                print('Player2 has WON!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE game')
                    break
                else:
                    turn='Player1'
    if not replay():
        braek








