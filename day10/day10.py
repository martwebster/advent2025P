# part 1
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


def get_fewest_joltages(lines):
    return sum([get_presses_joltage(line) for line in lines])


# part 2
def get_presses_joltage(line):
    result = line[1 : line.index("]")]
    buttonStr = line[line.index("]") + 2 : line.index("{") - 1]
    buttonArr = buttonStr.split(" ")
    buttons = [[int(x) for x in but[1:-1].split(",")] for but in buttonArr]

    joltageString = line[line.index("{") + 1 : -1]
    desiredJoltage = joltageString.split(",")
    initial = [0] * len(desiredJoltage)
    intialStr = ",".join(map(str, initial))
    joltages = {intialStr}

    preses = 0

    while not any(joltage == joltageString for joltage in joltages):
        joltages = {
            result
            for joltage in joltages
            for result in press_all_jottage_buttons(joltage, buttons)
        }
        preses += 1

    return preses


def press_all_jottage_buttons(joltage, buttons):
    result = []
    for button in buttons:
        result.append(press_joltage_button(joltage, button))
    return result


def press_joltage_button(joltage, button):
    result = [int(x) for x in joltage.split(",")]
    for toggle in button:
        result[toggle] = result[toggle] + 1
    resultSr = ",".join(map(str, result))
    return resultSr
