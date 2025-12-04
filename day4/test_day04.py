from day4.day04 import canAccess, get_positions, remove_all_rolls, remove_rolls


def test_example_part1():

    sample_input = readFile("day4/sample.txt").splitlines()
    assert canAccess(sample_input, 2, 0) == True
    assert get_positions(sample_input) == 13


def test_part1():
    sample_input = readFile("day4/input.txt").splitlines()
    assert get_positions(sample_input) == 1464


def test_example_part2():
    sample_input = readFile("day4/sample.txt").splitlines()
    assert remove_all_rolls(sample_input) == 43


def test_part2():
    sample_input = readFile("day4/input.txt").splitlines()
    assert remove_all_rolls(sample_input) == 8409


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
