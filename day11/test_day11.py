from day11.day11 import (
    count_to_outs,
    get_config,
    server_to_out,
)


def test_example_part1():
    data = readFile("day11/sample.txt").splitlines()
    config = get_config(data)
    outs = count_to_outs(config)
    assert outs == 5


def test_part1():
    data = readFile("day11/input.txt").splitlines()
    config = get_config(data)
    outs = count_to_outs(config)
    assert outs == 552


def test_example_part2():
    data = readFile("day11/sample2.txt").splitlines()
    config = get_config(data)
    outs = server_to_out(config)
    assert outs == 2


def test_part2():
    data = readFile("day11/input.txt").splitlines()
    config = get_config(data)
    outs = server_to_out(config)
    print(f"\nActual result: {outs}")
    assert outs == 307608674109300


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
