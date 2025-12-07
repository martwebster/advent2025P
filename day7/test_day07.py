from day7.day07 import get_beams, total_beams


def test_example_part1():
    data = readFile("day7/sample.txt").splitlines()

    assert total_beams(data) == 21


def test_part1():
    data = readFile("day7/input.txt").splitlines()

    assert total_beams(data) == 1541


def test_example_part2():
    data = readFile("day7/sample.txt").splitlines()

    assert get_beams(data) == 40


def test_part2():
    data = readFile("day7/input.txt").splitlines()

    assert get_beams(data) == 80158285728929


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
