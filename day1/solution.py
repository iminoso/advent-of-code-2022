import heapq


def part_1() -> int:
    with open("./input.txt", "r") as file:
        count = 0
        max_count = 0
        for line in file:
            if l := line.strip():
                count += int(l)
            else:
                max_count = max(count, max_count)
                count = 0
    return max_count


def part_2() -> int:
    with open("./input.txt", "r") as file:
        hp = []
        count = 0
        for line in file:
            if l := line.strip():
                count += int(l)
            else:
                heapq.heappush(hp, -1 * count)
                count = 0

        total = 0
        for _ in range(3):
            total += -1 * heapq.heappop(hp)
    return total


print(part_1())
print(part_2())
