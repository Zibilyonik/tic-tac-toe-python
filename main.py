combined_string = input()
line_1 = combined_string[:3]
line_2 = combined_string[3:6]
line_3 = combined_string[6:]
column_1 = line_1[0] + line_2[0] + line_3[0]
column_2 = line_1[1] + line_2[1] + line_3[1]
column_3 = line_1[2] + line_2[2] + line_3[2]
diagonal_1 = line_1[0] + line_2[1] + line_3[2]
diagonal_2 = line_1[2] + line_2[1] + line_3[0]
board = [line_1, line_2, line_3]
symbols = ["X", "O"]
print("---------")
print("|", line_1[0], line_1[1], line_1[2], "|")
print("|", line_2[0], line_2[1], line_2[2], "|")
print("|", line_3[0], line_3[1], line_3[2], "|")
print("---------")
def check_win(symbol):
    if symbol * 3 in [line_1, line_2, line_3, column_1, column_2, column_3, diagonal_1, diagonal_2]:
        return True
    else:
        return False

if (abs(combined_string.count(symbols[0]) - combined_string.count(symbols[1])) > 1) or (check_win("X") and check_win("O")):
    print("Impossible")
elif (not check_win("X") and not check_win("O")) and ("_" or " ") not in combined_string:
    print("Draw")
elif check_win(symbols[0]):
    print(symbols[0], "wins")
elif check_win(symbols[1]):
    print(symbols[1], "wins")
else:
    print("Game not finished")
    