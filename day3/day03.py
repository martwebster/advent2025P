def getJoltage(data):
    # 987654321111111
    int_array = [int(x) for x in data]

    max_value = max(int_array)

    val = ""
    if max_value == int_array[-1]:
        int_array.remove(max_value)
        next_value = max(int_array)
        val = int(str(next_value) + str(max_value))
    else:
        pos = int_array.index(max_value)
        int_array = int_array[pos + 1 :]
        next_value = max(int_array)
        val = int(str(max_value) + str(next_value))
    return val


def getTotalVolage(banks):
    return sum(map(getJoltage, banks.splitlines()))


def solve_part2(data):
    """
    Placeholder for Day 3 Part 2 solution.

    Args:
        data: Input data for the puzzle

    Returns:
        Solution for part 2
    """
    # TODO: Implement solution
    return 0


if __name__ == "__main__":
    # Read the actual puzzle input
    with open("day3/input.txt", "r") as f:
        puzzle_input = f.read().strip()

    # Solve both parts
    part1_answer = getJoltage(puzzle_input)
    part2_answer = solve_part2(puzzle_input)

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")
