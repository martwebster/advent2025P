from day11.day11 import (
    get_presses,
)


def test_example_part1():
    example = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    result = get_presses(example)
    assert result == 2

    assert (
        get_presses("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}") == 3
    )

    assert (
        get_presses("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}")
        == 2
    )


def test_part1():
    data = readFile("day10/input.txt").splitlines()
    result = get_fewest(data)
    assert result == 438


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
