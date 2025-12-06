from day6.day06 import getCoumnDefs, part_2, total_maths


def test_example_part1():
    data = readFile("day6/sample.txt").splitlines()

    assert total_maths(data) == 4277556


def test_part1():
    data = readFile("day6/input.txt").splitlines()

    assert total_maths(data) == 4878670269096


def test_example_part2():
    data = readFile("day6/sample.txt").splitlines()
    maxLength = max(len(line) for line in data)
    data = [line.ljust(maxLength) for line in data]
    cols = getCoumnDefs(data[3])

    assert part_2(data, cols) == 3263827


def test_part2():
    data = readFile("day6/input.txt").splitlines()
    maxLength = max(len(line) for line in data)
    data = [line.ljust(maxLength) for line in data]
    cols = getCoumnDefs(data[4])
    assert part_2(data, cols) == 8674740488592


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
