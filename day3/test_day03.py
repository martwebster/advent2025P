from day3.day03 import solve_part1, solve_part2


def test_example_part1():
    """Test Part 1 with sample input."""
    sample_input = readFile("day3/sample.txt")
    result = solve_part1(sample_input)
    # TODO: Update expected value once puzzle is available
    assert result == 0


def test_example_part2():
    """Test Part 2 with sample input."""
    sample_input = readFile("day3/sample.txt")
    result = solve_part2(sample_input)
    # TODO: Update expected value once puzzle is available
    assert result == 0


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
