def contains_overlap(a, b):
    a1, a2 = a
    b1, b2 = b
    if b1 <= a1 and a2 <= b2:
        return True
    elif a1 <= b1 and b2 <= a2:
        return True
    else:
        return False


def convert_tuple(raw_string):
    x, y = raw_string.split("-")
    return (int(x), int(y))


def part_1() -> int:
    count = 0
    with open("./input.txt", "r") as file:
        for line in file:
            l = line.strip()
            a_pair, b_pair = l.split(",")
            a, b = convert_tuple(a_pair), convert_tuple(b_pair)
            if contains_overlap(a, b):
                count += 1

    return count


def convert_set(t):
    return set([i for i in range(t[0], t[1] + 1)])


def part_2() -> int:
    count = 0
    with open("./input.txt", "r") as file:
        for line in file:
            l = line.strip()
            a_pair, b_pair = l.split(",")
            a, b = convert_tuple(a_pair), convert_tuple(b_pair)
            a_set = convert_set(a)
            b_set = convert_set(b)
            inter_set = a_set.intersection(b_set)
            if len(inter_set) > 0:
                count += 1

    return count


print(part_1())
print(part_2())
