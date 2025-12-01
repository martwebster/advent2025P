import pytest
from day1.day01 import getPasword, getPasword2


def testExamplePart1():
    output = readFile("day1/input.txt")
    directions = output.splitlines()
    assert getPasword(directions) == 3


def testPart1():
    result = getPasword(readFile("day1/part1.txt").splitlines())
    assert result == 1154  # Change to expected value


def testExamplePart2():
    result = getPasword2(readFile("day1/input.txt").splitlines())
    assert result == 6  # Change to expected value


def testPart2():
    result = getPasword2(readFile("day1/part1.txt").splitlines())
    assert result == 6819  # Change to expected value


def readFile(path):
    with open(path, "r") as f:
        puzzle_input = f.read().strip()
    return puzzle_input
