from types import *
import re

CARGO = [
    ["V", "C", "D", "R", "Z", "G", "B", "W"],
    ["G", "W", "F", "C", "B", "S", "T", "V"],
    ["C", "B", "S", "N", "W"],
    ["Q", "G", "M", "N", "J", "V", "C", "P"],
    ["T", "S", "L", "F", "D", "H", "B"],
    ["J", "V", "T", "W", "M", "N"],
    ["P", "F", "L", "C", "S", "T", "G"],
    ["B", "D", "Z"],
    ["M", "N", "Z", "W"],
]


def parse_input():
    # TODO parse this input properly
    cargo = [row[:] for row in CARGO]
    moves = []
    with open("./input.txt", "r") as file:
        for line in file:
            if "move" in line:
                match = re.search(
                    "move (?P<move>\d+) from (?P<src>\d+) to (?P<dest>\d+)", line
                )
                moves.append(
                    (
                        int(match.group("move")),
                        int(match.group("src")) - 1,
                        int(match.group("dest")) - 1,
                    )
                )

    return cargo, moves


def move_cargo(cargo, move_set):
    move, src, dest = move_set
    moving = []
    for _ in range(move):
        moving.append(cargo[src].pop())
    cargo[dest] += moving


def part_1() -> str:
    cargo, moves = parse_input()
    for move_set in moves:
        move_cargo(cargo, move_set)
    res = ""
    for c in cargo:
        res += c[-1]
    return res


def move_cargo_part_2(cargo, move_set):
    move, src, dest = move_set
    moving = []
    for _ in range(move):
        moving.append(cargo[src].pop())
    moving.reverse()
    cargo[dest] += moving


def part_2() -> str:
    cargo, moves = parse_input()
    for move_set in moves:
        move_cargo_part_2(cargo, move_set)
    res = ""
    for c in cargo:
        res += c[-1]
    return res


print(part_1())
print(part_2())
