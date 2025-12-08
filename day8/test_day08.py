from day8.day08 import total_beams


def test_example_part1():
    data = readFile("day8/sample.txt").splitlines()

    assert total_beams(data) == 21


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
