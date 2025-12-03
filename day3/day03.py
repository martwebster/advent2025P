def getJoltage(data):
    #987654321111111

    top_two = [int(x) for x in data]
    top_two.sort(reverse=True)
    top_two = top_two[:2]

    result = ""
    for x in data:
        if int(x) in top_two:
            result = result + x 
            top_two.remove(int(x))

    print(result)
    return int(result)

def getTotalVolage(banks):
    return sum(map(getJoltage,banks.splitlines()))


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
