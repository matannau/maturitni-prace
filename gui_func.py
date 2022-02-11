def create_points_vertical(WIDTH, HEIGHT):
    start_points = []
    end_points = []
    x = 0
    y = WIDTH / 10
    for _ in range(9):
        x += y
        start_points.append((x, 0))
        end_points.append((x, HEIGHT))

    return start_points, end_points


def create_points_horizontal(WIDTH, HEIGHT):
    start_points = []
    end_points = []
    x = 0
    y = HEIGHT / 10
    for _ in range(9):
        x += y
        start_points.append((0, x))
        end_points.append((WIDTH, x))

    return start_points, end_points

def load_grid(grid, size):
    print("    0    1    2    3    4    5    6    7    8    9")
    for i in range(size):
        for j in range(size):
            if j == 0:
                print(i, grid[i][j], end="")
            elif j == size - 1:
                print(grid[i][j])
            else:
                print(grid[i][j], end="")

    print("\n")

def place_symbol(grid, symbol, coordinates):
    if grid[coordinates[0]][coordinates[1]] == ["_"]:
        grid[coordinates[0]][coordinates[1]] = [symbol]
        return True
    else:
        print("You can not chose this spot\n")
        return False