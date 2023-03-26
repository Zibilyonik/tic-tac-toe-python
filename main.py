# Description: Tic-Tac-Toe game in Python
import string

board_state = ["___", "___", "___"]
symbols = ["X", "O"]


def print_board(board):
    print("---------")
    print("|", board[0][0], board[0][1], board[0][2], "|")
    print("|", board[1][0], board[1][1], board[1][2], "|")
    print("|", board[2][0], board[2][1], board[2][2], "|")
    print("---------")

def user_play(symbol):
    played = False
    while not played:
        line_input, column_input = input().split()
        if line_input not in string.digits or column_input not in string.digits:
            print("You should enter numbers!")
        elif int(line_input) not in range(1, 4) or int(column_input) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
        elif board_state[int(line_input) - 1][int(column_input) - 1] in symbols:
            print("This cell is occupied! Choose another one!")
        else:
            board_state[int(line_input) - 1] = board_state[int(line_input) - 1][:int(column_input) - 1] + str(symbols[symbol]) + board_state[int(line_input) - 1][int(column_input):]
            played = True
            print_board(board_state)
def check_win(symbol):
    """_check_win_
    Args:
        symbol (_string_): _player symbol_ (default: {_})

    Returns:
        _bool_: _if symbol won or not_
    """
    if symbol * 3 in [
        board_state[0],
        board_state[1],
        board_state[2],
        board_state[0][0] + board_state[1][0] + board_state[2][0],
        board_state[0][1] + board_state[1][1] + board_state[2][1],
        board_state[0][2] + board_state[1][2] + board_state[2][2],
        board_state[0][0] + board_state[1][1] + board_state[2][2],
        board_state[0][2] + board_state[1][1] + board_state[2][0],
    ]:
        return True
    else:
        return False

def check_draw():
    if (not check_win("X") and not check_win("O")) and (
    "_" or " "
) not in board_state[0] and ("_" or " ") not in board_state[1] and (
    "_" or " " ) not in board_state[2]:
        return True


def main():
    user_num = 0
    print_board(board_state)
    while True:
        user_play(user_num)
        if any([check_win("X"), check_win("O"), check_draw()]):
            if check_win("X"):
                print("X wins")
                return
            elif check_win("O"):
                print("O wins")
                return
            else:
                print("Draw")
                return
        user_num = (user_num + 1) % 2
        


main()