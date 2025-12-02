from day2.day02 import get_invalidIds, get_invalidIds2


sampleIds = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""


def testExamplePart1():
    assert get_invalidIds(sampleIds.strip()) == 1227775554


def testPart1():
    result = get_invalidIds(readFile("day2/notes.txt"))
    print(result)
    assert result == 28844599675


def testExamplePart2():
    assert get_invalidIds2(sampleIds.strip()) == 4174379265


def testPart2():
    result = get_invalidIds2(readFile("day2/notes.txt"))
    print(result)
    assert result == 48778605167


def readFile(path):
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
