grid = [[".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]]

actions = {
    "small ship": 1,
    "submarine": 2,
    "battleship": 3, 
}

def place_ships():
    for ship in actions:
        row = int(input("0-4: "))
        col = int(input("0-4: "))
        dir = int(input("Up(1) Down (2):"))
        grid[row][col] = "o"
        for i in ship:
            grid[row - 1][col] = "o"
        
    print(grid)

place_ships()