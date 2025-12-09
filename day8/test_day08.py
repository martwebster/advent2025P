from day8.day08 import build_boxes, build_circuit, part1, part2


def test_example_part1():
    data = readFile("day8/sample.txt").splitlines()
    boxes = build_boxes(data)
    points = build_circuit(boxes, 10)
    result = part1(points)
    assert result == 40


def test_part1():
    data = readFile("day8/input.txt").splitlines()
    boxes = build_boxes(data)
    points = build_circuit(boxes, 1000)
    result = part1(points)
    assert result == 122430


def test_example_part2():
    data = readFile("day8/sample.txt").splitlines()
    boxes = build_boxes(data)
    joins = build_circuit(boxes, 100000)
    i = 0
    for box in boxes:
        i = i + 1
        refs = [join for join in joins if join.source == box.id or join.dest == box.id]
        print(i, box, len(refs))

    result = part2(joins, boxes)

    assert result == 25272


def test_part2():
    data = readFile("day8/input.txt").splitlines()
    boxes = build_boxes(data)
    joins = build_circuit(boxes, 10000)
    result = part2(joins, boxes)
    assert result == 8135565324


# 813008 is too low. took 3 mins 42 seconds to run


def readFile(path):
    """Helper function to read input files."""
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
