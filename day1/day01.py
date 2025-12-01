def getPasword(data):
    pos = 50
    passwordCount = 0
    for direction in data:
        step = int(direction[1:]) % 100
        if direction[0] == "L":
            pos = pos - step
        if direction[0] == "R":
            pos = pos + step
        if pos < 0:
            pos = 100 + pos
        if pos > 99:
            pos = pos - 100
        if pos == 0:
            passwordCount = passwordCount + 1
    return passwordCount


def getPasword2(data):
    pos = 50
    passwordCount = 0
    for direction in data:
        step = int(direction[1:])
        for i in range(step):
            if direction[0] == "L":
                pos = pos - 1
            else:
                pos = pos + 1
            if pos == -1:
                pos = 99
            if pos == 100:
                pos = 0
            if pos == 0:
                passwordCount = passwordCount + 1
    return passwordCount


if __name__ == "__main__":
    # Read the actual puzzle input
    with open("day1/part1.txt", "r") as f:
        puzzle_input = f.read().strip()

    directions = puzzle_input.splitlines()

    # Solve both parts
    part1_answer = getPasword(directions)
    part2_answer = getPasword2(directions)

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")
