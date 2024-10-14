grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
gameOn = True
turn = 1

def print_screen():
    for ix, r in enumerate(grid):
        row = ''
        for iy, cell in enumerate(r):
            row += f' {cell} '
            if iy < 2:
                row += f' | '
        print(row)
        if ix < 2:
            print('---------------')


def make_move(cell):
    row = (cell - 1) // 3
    col = (cell - 1) % 3

    if not grid[row][col] == ' ':
        print("invalid move")
        return False

    grid[row][col] = char
    return True

def check_game():
    if turn < 5:
        return True
    elif turn == 9:
        if not check_for_win():
            print('The game is a tie!')
            return False
    else:
        return not check_for_win()

def check_for_win():
    # check rows
    has_win = False
    if grid[0][0] == char and grid[0][1] == char and grid[0][2] == char:
        print(f'Player {player} wins!')
        has_win = True
    elif grid[1][0] == char and grid[1][1] == char and grid[1][2] == char:
        print(f'Player {player} wins!')
        has_win = True
    elif grid[2][0] == char and grid[2][1] == char and grid[2][2] == char:
        print(f'Player {player} wins!')
        has_win = True

    # check columns
    elif grid[0][0] == char and grid[1][0] == char and grid[2][0] == char:
        print(f'Player {player} wins!')
        has_win = True
    elif grid[0][1] == char and grid[1][1] == char and grid[2][1] == char:
        print(f'Player {player} wins!')
        has_win = True
    elif grid[0][2] == char and grid[1][2] == char and grid[2][2] == char:
        print(f'Player {player} wins!')
        has_win = True

    # check diagonals
    elif grid[0][0] == char and grid[1][1] == char and grid[2][2] == char:
        print(f'Player {player} wins!')
        has_win = True
    elif grid[0][2] == char and grid[1][1] == char and grid[2][0] == char:
        print(f'Player {player} wins!')
        has_win = True

    # print_screen()
    return has_win


print_screen()

while gameOn:
    player = ((turn - 1) % 2) + 1
    char = 'X' if player == 1 else 'O'
    move = input(f'player {player} make your move ({char}):')

    if make_move(int(move)):
        gameOn = check_game()
        print_screen()
        turn += 1

input('enter to exit')

