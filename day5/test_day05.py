from day5.day05 import count_fresh, get_range


def test_example_part1():
    sample_input = readFile("day5/sample.txt").splitlines()
    fresh_list = sample_input[: sample_input.index("")]
    ingredients = sample_input[sample_input.index("") + 1 :]
    assert count_fresh(fresh_list, ingredients) == 3


def test_part1():
    sample_input = readFile("day5/input.txt").splitlines()
    fresh_list = sample_input[: sample_input.index("")]
    ingredients = sample_input[sample_input.index("") + 1 :]
    assert count_fresh(fresh_list, ingredients) == 874


def test_example_part2():
    sample_input = readFile("day5/sample.txt").splitlines()
    fresh_list = sample_input[: sample_input.index("")]
    assert get_range(fresh_list) == 14


def test_part2():
    sample_input = readFile("day5/input.txt").splitlines()
    fresh_list = sample_input[: sample_input.index("")]
    assert get_range(fresh_list) == 348548952146313


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
