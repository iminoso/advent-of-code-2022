import string


def generate_map():
    value = 1
    item_value = {}
    for c in string.ascii_letters:
        item_value[c] = value
        value += 1
    return item_value


def part_1() -> int:
    item_value_map = generate_map()
    with open("./input.txt", "r") as file:
        items = []
        score = 0

        for line in file:
            l = line.strip()
            first_rucksack = set(l[: (len(l) // 2)])
            for c in l[(len(l) // 2) :]:
                if c in first_rucksack:
                    items.append(c)
                    break

        for i in items:
            score += item_value_map[i]

    return score


def part_2() -> int:
    item_value_map = generate_map()
    with open("./input.txt", "r") as file:
        items = []
        score = 0
        word_sets = []
        for line in file:
            l = line.strip()
            word_sets.append(set(l))

            if len(word_sets) == 3:
                first, second, third = word_sets
                inter = (first.intersection(second)).intersection(third)
                items.append([i for i in inter][0])
                word_sets = []

        for i in items:
            score += item_value_map[i]

    return score


print(part_1())
print(part_2())
