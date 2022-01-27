import random

def create_grid(size):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(["_"])
        
        grid.append(row)

    return grid, size

def load_grid(grid, size):
    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print(grid[i][j])
            else:
                print(grid[i][j], end="")

    print("\n")

def place_symbol(grid, symbol, coordinates):
    if grid[coordinates[0]][coordinates[1]] == ["_"]:
        grid[coordinates[0]][coordinates[1]] = [symbol]
    else:
        print("You can not chose this spot")

def check_spaces(i, j, size, grid, player_symbol):
    if i >= 0 and j >= 0 and i < size and j < size and grid[i][j] != [player_symbol]:
        return True
    return False

def check_if_empty(i, j, size, grid):
    if i >= 0 and j >= 0 and i < size and j < size and grid[i][j] == ["_"]:
        return True
    return False

def loop_increment_basic(i, j, size, grid, player_symbol):
    possible_move = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            if not (x == y == 0):
                if check_if_empty(i + y, j + x, size, grid) and check_spaces(i + 4*y, j + 4*x, size, grid, "X"):
                    move = check_potential_development(i, j, grid, "X", y, x)
                    if move not in possible_move:
                        possible_move.append(move)

    return possible_move

def loop_increment_primary(i, j, size, grid, player_symbol):
    value = 8
    for y in range(-1, 2):
        for x in range(-1, 2):
            if not check_spaces(i + y, j + x, size, grid, player_symbol):
                value -= 1
    
    return value


def check_potential_development(i, j, grid, player_symbol, y, x):
    # y -> i, x -> j
    value = 0
    for num in range(1, 5):
        space = grid[i + num * y][j + num * x]
        if space == ["_"]:
            value += 1
        elif space == [player_symbol]:
            value += 10
            break
    
    move = [i, j, value]
    return move


def find_primary_value(grid, size):
    possible_moves = []
    best_value = float("-inf")
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["_"]:
                value = loop_increment_primary(i, j, size, grid, "X")

                if value > best_value:
                    best_value = value
                possible_moves.append([i, j, value])

                # grid[i][j] = [value]
 
    return best_value, possible_moves


def find_move_value(grid, size):
    possible_moves = []
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["_"]:
                possible_moves.extend(loop_increment_basic(i, j, size, grid, "X"))

                
                
    print(len(possible_moves))  
    return possible_moves



def get_move(best_value, possible_moves):
    best_moves = []
    x = len(possible_moves)
    for i in range(x - 1):
        if possible_moves[i][2] == best_value:
            best_moves.append(possible_moves[i])

    return random.choice(best_moves)

'''
Tests :)
'''

# gamegrid, size = create_grid(10)
# place_symbol(gamegrid, "X", [5, 4, 4])
# x, y, grid = find_primary_value(gamegrid, size)
# load_grid(grid, size)
# size = 10
# i, j = 6, 7
# print(find_move_value(gamegrid, size))
# print(check_spaces(i, j + 1, size, gamegrid, "X"))
# print(check_if_empty(i, j + 4, size, gamegrid))