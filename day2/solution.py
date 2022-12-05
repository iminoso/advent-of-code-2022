PICK_MAP = {"X": 1, "Y": 2, "Z": 3}
RESULT_POINT_MAP = {"T": 3, "W": 6, "L": 0}


def part_1() -> int:
    RESULT_MAP = {
        ("A", "X"): "T",
        ("A", "Y"): "W",
        ("A", "Z"): "L",
        ("B", "X"): "L",
        ("B", "Y"): "T",
        ("B", "Z"): "W",
        ("C", "X"): "W",
        ("C", "Y"): "L",
        ("C", "Z"): "T",
    }
    with open("./input.txt", "r") as file:
        score = 0
        for line in file:
            l = line.strip()
            opponent_pick, my_pick = l.split(" ")
            pick_score = PICK_MAP[my_pick]
            result = RESULT_MAP[(opponent_pick, my_pick)]
            result_score = RESULT_POINT_MAP[result]
            score += pick_score + result_score
    return score


def part_2() -> int:
    RESULT_MAP = {
        ("A", "X"): ("Z", 0),
        ("A", "Y"): ("X", 3),
        ("A", "Z"): ("Y", 6),
        ("B", "X"): ("X", 0),
        ("B", "Y"): ("Y", 3),
        ("B", "Z"): ("Z", 6),
        ("C", "X"): ("Y", 0),
        ("C", "Y"): ("Z", 3),
        ("C", "Z"): ("X", 6),
    }
    with open("./input.txt", "r") as file:
        score = 0
        for line in file:
            l = line.strip()
            opponent_pick, result = l.split(" ")
            my_pick, result_score = RESULT_MAP[(opponent_pick, result)]
            my_score = PICK_MAP[my_pick]
            score += result_score + my_score
    return score


print(part_1())
print(part_2())
