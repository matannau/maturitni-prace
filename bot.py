import random


gamegrid = [
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
]

size = 10

def loadgrid(grid):
    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print(grid[i][j])
            else:
                print(grid[i][j], end="")

def checkSpaces(i, j, size, grid):
    if i >= 0 and j >= 0 and i < size and j < size and grid[i][j] != ["X"]:
        return True
    return False

def findPrimaryValue(grid):
    possible_moves = []
    best_value = float("-inf")
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["_"]:
                value = 8
                if not checkSpaces(i, j - 1, size, grid):
                    value -= 1
                if not checkSpaces(i, j + 1, size, grid):
                    value -= 1
                if not checkSpaces(i - 1, j, size, grid):
                    value -= 1
                if not checkSpaces(i + 1, j, size, grid):
                    value -= 1
                if not checkSpaces(i - 1, j - 1, size, grid):
                    value -= 1
                if not checkSpaces(i - 1, j + 1, size, grid):
                    value -= 1
                if not checkSpaces(i + 1, j - 1, size, grid):
                    value -= 1
                if not checkSpaces(i + 1, j + 1, size, grid):
                    value -= 1
                
                if value > best_value:
                    best_value = value
                
                possible_moves.append([i, j, value])
                
    return best_value, possible_moves


def getInitialMove(best_value, possible_moves):
    best_moves = []
    for i in range(pow(size, 2) - 1):
        if possible_moves[i][2] == best_value:
            best_moves.append(possible_moves[i])

    return random.choice(best_moves)

x, y = findPrimaryValue(gamegrid)
print(getInitialMove(x, y))
