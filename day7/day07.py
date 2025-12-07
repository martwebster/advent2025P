from dataclasses import dataclass


@dataclass
class Pos:
    x: int
    y: int
    count: int


# Part 1
def total_beams(lines: list, debug=False):

    beams = [Pos(lines[0].index("S"), 0, 1)]

    total = 0
    while max(pos.y for pos in beams) < len(lines) - 1:
        before = len(beams)
        beams = [new_pos for pos in beams for new_pos in _move(lines, pos)]
        after = len(beams)
        total = total + (after - before)

        beams = list(set((pos.x, pos.y, pos.count) for pos in beams))
        beams = [Pos(x, y, count) for x, y, count in beams]
        if debug:
            print_beams(lines, beams)
    return total


def print_beams(lines: list, beams: list):
    print("")
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if Pos(x, y) in beams:
                print("|", end="")
            else:
                print(lines[y][x], end="")
        print("")


def _move(lines: list, pos: Pos):

    pos = Pos(pos.x, pos.y + 1, pos.count)
    next = lines[pos.y][pos.x]
    if next == ".":
        return [pos]
    if next == "^":
        return [Pos(pos.x - 1, pos.y, pos.count), Pos(pos.x + 1, pos.y, pos.count)]
    else:
        raise ValueError(f"Unknown character: {next}")


# Part 2 - Not to prune the BFS, so that we include a count of how they got there
def get_beams(lines: list):

    beams = [Pos(lines[0].index("S"), 0, 1)]

    while max(pos.y for pos in beams) < len(lines) - 1:
        # Python version of a flatmap
        beams = [new_pos for pos in beams for new_pos in _move(lines, pos)]
        beams = merge_beams(beams)
    return sum(beam.count for beam in beams)


def merge_beams(beams: list):
    # Dictionary can be used to ensure uniqueness, and sum total
    beam_dict = {}
    for beam in beams:
        key = (beam.x, beam.y)
        if key in beam_dict:
            beam_dict[key].count += beam.count
        else:
            beam_dict[key] = beam
    return list(beam_dict.values())
