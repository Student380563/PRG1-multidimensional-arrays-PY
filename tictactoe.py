grid = [[".",".", ".", "."],
        [".",".", ".", "."],
        [".",".", ".", "."],
        [".",".", ".", "."]]

def board(grid):
    print(["0","1","2","3"])
    for i in range(4):
        print(grid[i])

def player_move(row, col, player):
    grid[row][col] = player

win = False
cross = "x"
circle = "o"
player = cross

while not win:
    print("_____current board_____")
    board(grid)
    row = int(input("input row: "))
    col = int(input("input col: "))
    player_move(row, col, player)
    board(grid)
    if player == cross:
        player = circle
    else:
        player = cross