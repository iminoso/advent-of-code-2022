def build_grid():
    tree_grid = []
    with open("./input.txt", "r") as file:
        for line in file:
            line = line.strip()
            tree_grid.append([int(l) for l in line])
    return tree_grid


def check_visibility(r_i, c_i, tree_grid):
    curr = tree_grid[r_i][c_i]

    valid = True
    i = r_i - 1
    while i >= 0:
        if tree_grid[i][c_i] >= curr:
            valid = False
            break
        i -= 1
    if valid:
        return True

    valid = True
    i = c_i - 1
    while i >= 0:
        if tree_grid[r_i][i] >= curr:
            valid = False
            break
        i -= 1
    if valid:
        return True

    valid = True
    i = r_i + 1
    while i < len(tree_grid):
        if tree_grid[i][c_i] >= curr:
            valid = False
            break
        i += 1
    if valid:
        return True

    valid = True
    i = c_i + 1
    while i < len(tree_grid[r_i]):
        if tree_grid[r_i][i] >= curr:
            valid = False
            break
        i += 1
    if valid:
        return True

    return False


def part_1() -> int:
    tree_grid = build_grid()
    count = len(tree_grid) * 2 + (len(tree_grid[0]) - 2) * 2
    for r_i in range(1, len(tree_grid) - 1):
        for c_i in range(1, len(tree_grid[r_i]) - 1):
            if check_visibility(r_i, c_i, tree_grid):
                count += 1
    return count


def check_scenic(r_i, c_i, tree_grid):
    curr = tree_grid[r_i][c_i]

    total = 0
    curr_scenic = 0
    i = r_i - 1
    while i >= 0:
        curr_scenic += 1
        if tree_grid[i][c_i] >= curr:
            break
        i -= 1
    total = curr_scenic

    curr_scenic = 0
    i = c_i - 1
    while i >= 0:
        curr_scenic += 1
        if tree_grid[r_i][i] >= curr:
            break
        i -= 1
    total *= curr_scenic

    curr_scenic = 0
    i = r_i + 1
    while i < len(tree_grid):
        curr_scenic += 1
        if tree_grid[i][c_i] >= curr:
            break
        i += 1
    total *= curr_scenic

    curr_scenic = 0
    i = c_i + 1
    while i < len(tree_grid[r_i]):
        curr_scenic += 1
        if tree_grid[r_i][i] >= curr:
            break
        i += 1
    total *= curr_scenic

    return total


def part_2() -> int:
    tree_grid = build_grid()
    max_scenic_score = 0
    for r_i in range(1, len(tree_grid) - 1):
        for c_i in range(1, len(tree_grid[r_i]) - 1):
            max_scenic_score = max(max_scenic_score, check_scenic(r_i, c_i, tree_grid))
    return max_scenic_score


print(part_1())
print(part_2())
