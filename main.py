# Description: Tic-Tac-Toe game in Python
import string

combined_string = input()
line_1 = combined_string[:3]
line_2 = combined_string[3:6]
line_3 = combined_string[6:]
column_1 = line_1[0] + line_2[0] + line_3[0]
column_2 = line_1[1] + line_2[1] + line_3[1]
column_3 = line_1[2] + line_2[2] + line_3[2]
diagonal_1 = line_1[0] + line_2[1] + line_3[2]
diagonal_2 = line_1[2] + line_2[1] + line_3[0]
board_state = [line_1, line_2, line_3]
symbols = ["X", "O"]


def print_board(board):
    print("---------")
    print("|", board[0][0], board[0][1], board[0][2], "|")
    print("|", board[1][0], board[1][1], board[1][2], "|")
    print("|", board[2][0], board[2][1], board[2][2], "|")
    print("---------")

def user_play():
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
            board_state[int(line_input) - 1] = board_state[int(line_input) - 1][:int(column_input) - 1] + symbols[0] + board_state[int(line_input) - 1][int(column_input):]
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
        line_1,
        line_2,
        line_3,
        column_1,
        column_2,
        column_3,
        diagonal_1,
        diagonal_2,
    ]:
        return True
    else:
        return False


# if (abs(combined_string.count(symbols[0]) - combined_string.count(symbols[1])) > 1) or (
#     check_win("X") and check_win("O")
# ):
#     print("Impossible")
# elif (not check_win("X") and not check_win("O")) and (
#     "_" or " "
# ) not in combined_string:
#     print("Draw")
# elif check_win(symbols[0]):
#     print(symbols[0], "wins")
# elif check_win(symbols[1]):
#     print(symbols[1], "wins")
# else:
#     print("Game not finished")

print_board(board_state)
user_play()
