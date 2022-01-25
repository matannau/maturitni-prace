import random

# def create_grid(size):
#     grid = []
#     for i in range(size):
#         row = []
#         for j in range(size):
#             row.append(["_"])
        
#         grid.append(row)

#     return grid, size

# def load_grid(grid, size):
#     for i in range(size):
#         for j in range(size):
#             if j == size - 1:
#                 print(grid[i][j])
#             else:
#                 print(grid[i][j], end="")

#     print("\n")

# def place_symbol(grid, symbol, coordinates):
#     if grid[coordinates[0]][coordinates[1]] == ["_"]:
#         grid[coordinates[0]][coordinates[1]] = [symbol]
#     else:
#         print("You can not chose this spot")

def check_spaces(i, j, size, grid, player_symbol):
    if i >= 0 and j >= 0 and i < size and j < size and grid[i][j] != [player_symbol]:
        return True
    return False

def check_potential_development(i, j, size, grid, computer_symbol):
    if i >= 0:
        pass

def find_primary_value(grid, size):
    possible_moves = []
    best_value = float("-inf")
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["_"]:
                value = 8
                if not check_spaces(i, j - 1, size, grid, "X"):
                    value -= 1
                if not check_spaces(i, j + 1, size, grid, "X"):
                    value -= 1
                if not check_spaces(i - 1, j, size, grid, "X"):
                    value -= 1
                if not check_spaces(i + 1, j, size, grid, "X"):
                    value -= 1
                if not check_spaces(i - 1, j - 1, size, grid, "X"):
                    value -= 1
                if not check_spaces(i - 1, j + 1, size, grid, "X"):
                    value -= 1
                if not check_spaces(i + 1, j - 1, size, grid, "X"):
                    value -= 1
                if not check_spaces(i + 1, j + 1, size, grid, "X"):
                    value -= 1
                
                if value > best_value:
                    best_value = value
                possible_moves.append([i, j, value])

                # grid[i][j] = [value]
 
    return best_value, possible_moves


def find_move_value(grid, size):
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["_"]:

                # Checks if left side is suitable for playing
                if check_spaces(i, j + 1, size, grid, "_"):
                    pass



def get_move(best_value, possible_moves):
    best_moves = []
    x = len(possible_moves)
    for i in range(x - 1):
        if possible_moves[i][2] == best_value:
            best_moves.append(possible_moves[i])

    return random.choice(best_moves)

# gamegrid, size = create_grid(5)
# place_symbol(gamegrid, "X", [2, 3, 3])
# x, y, grid = find_primary_value(gamegrid, size)
# load_grid(grid, size)