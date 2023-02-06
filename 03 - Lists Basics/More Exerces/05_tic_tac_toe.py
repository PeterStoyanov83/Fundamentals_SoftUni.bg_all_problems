def tic_tac_toe(field):
    # check rows
    for row in field:
        if all(x == 1 for x in row):
            return "First player won"
        elif all(x == 2 for x in row):
            return "Second player won"

    # check columns
    for col in range(3):
        if all(field[row][col] == 1 for row in range(3)):
            return "First player won"
        elif all(field[row][col] == 2 for row in range(3)):
            return "Second player won"

    # check diagonals
    if all(field[i][i] == 1 for i in range(3)):
        return "First player won"
    elif all(field[i][i] == 2 for i in range(3)):
        return "Second player won"
    if all(field[i][2 - i] == 1 for i in range(3)):
        return "First player won"
    elif all(field[i][2 - i] == 2 for i in range(3)):
        return "Second player won"

    return "Draw!"


field = []
for i in range(3):
    field.append(list(map(int, input().split())))
print(tic_tac_toe(field))
