from day3.day03 import getJoltage, getTotalVolage


def test_example_part1():
    """Test Part 1 with sample input."""

    assert getJoltage("987654321111111") == 98

    assert getJoltage("811111111111119") == 89
    sample_input = readFile("day3/sample.txt")
    assert getTotalVolage(sample_input) == 357


def test_part1():
    sample_input = readFile("day3/input.txt")
    assert getTotalVolage(sample_input) == 17311


def test_example_part2():
    assert getJoltage("987654321111111", 12) == 987654321111
    assert getJoltage("811111111111119", 12) == 811111111119
    assert getJoltage("234234234234278", 12) == 434234234278
    assert getJoltage("818181911112111", 12) == 888911112111


def test_part2():
    sample_input = readFile("day3/input.txt")
    assert getTotalVolage(sample_input, 12) == 171419245422055


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
