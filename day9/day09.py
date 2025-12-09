from dataclasses import dataclass


@dataclass
class Pos:
    x: str
    y: int


def get_area(a: Pos, b: Pos):
    return abs(((b.x - a.x) + 1) * ((b.y - a.y) + 1))


def get_max_area(lines: list):
    positions = [
        Pos(int(line.split(",")[0]), int(line.split(",")[1])) for line in lines
    ]
    positions.sort(key=lambda c: c.x)

    max_area = 0
    for i, pos in enumerate(positions):
        for other in positions[i + 1 :]:
            if other.y != other.x:
                area = get_area(pos, other)
                max_area = max(max_area, area)

    print(positions)
    return max_area
