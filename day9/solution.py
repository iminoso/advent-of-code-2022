from typing import *


def is_touching(head_pos: Tuple[int, int], tail_pos: Tuple[int, int]) -> bool:
    hx, hy = head_pos
    tx, ty = tail_pos
    return abs(hx - tx) <= 1 and abs(hy - ty) <= 1


def move_tail(head_pos: Tuple[int, int], tail_pos: Tuple[int, int]) -> Tuple[int, int]:
    hx, hy = head_pos
    tx, ty = tail_pos

    if abs(hx - tx) == 2 and hy == ty:
        return (tx + (hx - tx) // 2, ty)
    elif hx == tx and abs(hy - ty) == 2:
        return (tx, ty + (hy - ty) // 2)
    else:
        #  diagonal movement
        if abs(hx - tx) == 2 and abs(hy - ty) == 1:
            return (tx + (hx - tx) // 2, hy)
        elif abs(hx - tx) == 1 and abs(hy - ty) == 2:
            return (hx, ty + (hy - ty) // 2)
        elif abs(hx - tx) == 2 and abs(hy - ty) == 2:
            return (tx + (hx - tx) // 2, ty + (hy - ty) // 2)


def get_direction(d: str) -> Tuple[int, int]:
    if d == "R":
        return (1, 0)
    elif d == "L":
        return (-1, 0)
    elif d == "U":
        return (0, 1)
    elif d == "D":
        return (0, -1)


def part_1() -> int:
    head_pos = (0, 0)
    tail_pos = (0, 0)
    visited = set([(0, 0)])
    with open("./input.txt", "r") as file:
        for line in file:
            line = line.strip()
            direction, steps = line.split(" ")
            dx, dy = get_direction(direction)
            for _ in range(int(steps)):
                hx, hy = head_pos
                head_pos = (hx + dx, hy + dy)
                if not is_touching(head_pos, tail_pos):
                    tail_pos = move_tail(head_pos, tail_pos)
                    visited.add(tail_pos)

    return len(visited)


ROPE = [(0, 0)] * 10


def part_2() -> int:
    visited = set([(0, 0)])
    with open("./input.txt", "r") as file:
        for line in file:
            line = line.strip()
            direction, steps = line.split(" ")
            dx, dy = get_direction(direction)
            for _ in range(int(steps)):
                hx, hy = ROPE[0]
                ROPE[0] = (hx + dx, hy + dy)

                for i in range(1, len(ROPE)):
                    prev = ROPE[i - 1]
                    curr = ROPE[i]
                    if not is_touching(prev, curr):
                        curr = move_tail(prev, curr)
                        ROPE[i] = curr
                    else:
                        break

                visited.add(ROPE[-1])
    return len(visited)


print(part_1())
print(part_2())
