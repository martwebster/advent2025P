from day1.day01 import get_password, get_password2


def test_example_part1():
    output = read_file("day1/input.txt")
    directions = output.splitlines()
    assert get_password(directions) == 3


def test_part1():
    result = get_password(read_file("day1/part1.txt").splitlines())
    print(result)
    assert result == 1154  # Change to expected value


def test_example_part2():
    result = get_password2(read_file("day1/input.txt").splitlines())
    assert result == 6  # Change to expected value


def test_part2():
    result = get_password2(read_file("day1/part1.txt").splitlines())
    assert result == 6819  # Change to expected value


def read_file(path):
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
