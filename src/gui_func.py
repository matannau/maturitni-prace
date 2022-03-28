def create_points_vertical(size, spots):
    # This function defines the spots where vertical
    # lines on the game grid should start and end
    start_points = []
    end_points = []
    x = 0
    y = size / spots
    for _ in range(spots - 1):
        x += y
        start_points.append((x, 0))
        end_points.append((x, size))

    return start_points, end_points


def create_points_horizontal(size, spots):
    # This function defines the spots where horizontal
    # lines on the game grid should start and end
    start_points = []
    end_points = []
    x = 0
    y = size / spots
    for _ in range(spots - 1):
        x += y
        start_points.append((0, x))
        end_points.append((size, x))

    return start_points, end_points


def place_symbol(grid, symbol, coordinates):
    # Places a symbol on the given coordinates if it is empty
    if grid[coordinates[0]][coordinates[1]] == ["_"]:
        grid[coordinates[0]][coordinates[1]] = [symbol]
        return True
    else:
        print("You can not chose this spot\n")
        return False
