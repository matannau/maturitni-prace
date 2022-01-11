from wincheck import check_lines, check_diagonals

gamegrid = [
[["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"]],
[["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["X"], ["_"], ["_"], ["X"], ["O"], ["X"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["X"], ["O"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["X"], ["X"], ["X"], ["X"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["O"], ["_"], ["X"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["X"], ["X"], ["X"], ["X"], ["_"], ["X"]],
[["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"]],
[["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["X"], ["O"], ["O"], ["O"]]
]

size = 10

def loadgrid(grid):
    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print(grid[i][j])
            else:
                print(grid[i][j], end="")


def check_win(grid):
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["X"]:
                if check_lines(i, j, "X", grid, size) == True:
                    return "X has won"
                if check_diagonals(i, j, "X", grid, size) == True:
                    return "X has won"
            if grid[i][j] == ["O"]:
                if check_lines(i, j, "O", grid, size) == True:
                    return "O has won"
                if check_diagonals(i, j, "O", grid, size) == True:
                    return "O has won"
    return "No one has won"

loadgrid(gamegrid)
print(check_win(gamegrid))