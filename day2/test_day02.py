from day2.day02 import getPasword


def testExamplePart1():
    output = readFile("day2/sample.txt")
    directions = output.splitlines()
    assert getPasword(directions) == 0


def testPart1():
    result = getPasword(readFile("day2/notes.txt").splitlines())
    print(result)
    assert result == 0


def readFile(path):
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
