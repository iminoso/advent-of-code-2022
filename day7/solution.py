from types import *
from collections import deque

SIZE = "_size"
FILE_MARKER = "_file"
FILE_SYS = {SIZE: 0}
THRESHOLD = 100000
TOTAL_SIZE = 70000000
REQUIRED_SIZE = 30000000


def parse_cd(cmd: str, path: list[str], current_dir: dict):
    _, move = cmd.split(" ")

    if move == "/":
        return [], FILE_SYS
    elif move == "..":
        target_dir = FILE_SYS
        for i in path[:-1]:
            target_dir = target_dir[i]
        path.pop()
        return path, target_dir
    else:
        path.append(move)
        return path, current_dir[move]


def parse_ls(line: str, dir: dict, path: list[str]):
    if "dir" in line:
        _, name = line.split(" ")
        dir[name] = {}
        dir[name][SIZE] = 0
    else:
        size, file_name = line.split(" ")
        size = int(size)
        dir[file_name] = {SIZE: size, FILE_MARKER: True}
        FILE_SYS[SIZE] += size
        size_dir = FILE_SYS
        for p in path:
            size_dir[p][SIZE] += size
            size_dir = size_dir[p]

    return dir


def find_dir():
    combined_size = 0
    queue = deque([FILE_SYS])
    while queue:
        d = queue.popleft()
        if d[SIZE] < THRESHOLD:
            combined_size += d[SIZE]

        for k in d:
            if k != SIZE and FILE_MARKER not in d[k]:
                queue.append(d[k])
    return combined_size


def part_1() -> int:
    path = []
    current_dir = FILE_SYS
    with open("./input.txt", "r") as file:
        for line in file:
            if "$" in line:
                cmd = line.strip("$").strip()
                if "cd" in cmd:
                    path, current_dir = parse_cd(cmd, path, current_dir)
                elif "ls" in cmd:
                    continue
            else:  # must be in ls output
                line = line.strip()
                current_dir = parse_ls(line, current_dir, path)
    return find_dir()


def part_2() -> int:
    required_delete = REQUIRED_SIZE - (TOTAL_SIZE - FILE_SYS[SIZE])
    min_delete = FILE_SYS[SIZE]
    queue = deque([FILE_SYS])
    while queue:
        d = queue.popleft()
        if d[SIZE] >= required_delete:
            min_delete = min(min_delete, d[SIZE])

        for k in d:
            if k != SIZE and FILE_MARKER not in d[k]:
                queue.append(d[k])

    return min_delete


print(part_1())
print(part_2())
