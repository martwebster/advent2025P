from dataclasses import dataclass


@dataclass
class Pos:
    x: str
    y: int


# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
def get_presses(line):
    result = line[1 : line.index("]")]
    buttonStr = line[line.index("]") + 2 : line.index("{") - 1]
    buttonArr = buttonStr.split(" ")
    buttons = [[int(x) for x in but[1:-1].split(",")] for but in buttonArr]

    initial = "." * len(result)
    indicators = {initial}

    preses = 0

    while not any(indicator == result for indicator in indicators):
        indicators = {
            result
            for indicator in indicators
            for result in press_all_buttons(indicator, buttons)
        }
        preses += 1

    return preses


def get_fewest(lines):
    return sum([get_presses(line) for line in lines])


def press_all_buttons(indicator, buttons):
    result = []
    for button in buttons:
        result.append(press_button(indicator, button))
    return result


def press_button(indicator, button):
    result = indicator
    for toggle in button:
        if result[toggle] == ".":
            result = result[:toggle] + "#" + result[toggle + 1 :]

        else:
            result = result[:toggle] + "." + result[toggle + 1 :]
    return result


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
