def getPasword(data):
    passwordCount = 0
    return passwordCount

if __name__ == "__main__":
    # Read the actual puzzle input
    with open("day2/notes.txt", "r") as f:
        puzzle_input = f.read().strip()

    directions = puzzle_input.splitlines()

    # Solve both parts
    part1_answer = getPasword(directions)

    print(f"Part 1: {part1_answer}")
