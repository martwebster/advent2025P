from day12.day12 import (
    get_present_count,
)


def test_part1():
    data = readFile("day12/input.txt")
    assert get_present_count(data) == 587


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
