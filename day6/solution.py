from types import *


def find_unique_sequence(sequence: str, sequence_length: int) -> int:
    s, e = 0, sequence_length - 1
    cache = {}
    for i in range(4):
        cache[sequence[i]] = cache.get(sequence[i], 0) + 1

    while len(cache) != sequence_length:
        cache[sequence[s]] = cache.get(sequence[s], 1) - 1
        if cache[sequence[s]] == 0:
            del cache[sequence[s]]
        s += 1
        e += 1
        cache[sequence[e]] = cache.get(sequence[e], 0) + 1

    return e + 1


def part_1() -> int:
    with open("./input.txt", "r") as file:
        seq = ""
        for line in file:
            seq = line
            break

        return find_unique_sequence(seq, 4)


def part_2() -> int:
    with open("./input.txt", "r") as file:
        seq = ""
        for line in file:
            seq = line
            break

        return find_unique_sequence(seq, 14)


print(part_1())
print(part_2())
