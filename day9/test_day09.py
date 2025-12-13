from day9.day09 import get_max_area, part_2


def test_example_part1():
    data = readFile("day9/sample.txt").splitlines()
    result = get_max_area(data)
    assert result == 50


def test_part1():
    data = readFile("day9/input.txt").splitlines()
    result = get_max_area(data)
    assert result == 4782151432


def test_part2():
    data = readFile("day9/input.txt").splitlines()
    result = part_2(data)
    assert result == 1450414119


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
