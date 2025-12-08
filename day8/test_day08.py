from day8.day08 import build_circuit, build_circuits, connect_points


def test_example_part1():
    data = readFile("day8/sample.txt").splitlines()
    points = build_circuit(data)
    connect_points(points, 10)
    result = build_circuits(points)
    assert result == 40


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
