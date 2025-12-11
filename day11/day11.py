from dataclasses import dataclass


@dataclass
class PathToOut:
    current: str
    previous: str = ""
    count: int = 1

    def move(self, place):
        new_path = PathToOut(
            current=place,
            previous=(
                self.previous + "-" + self.current if self.previous else self.current
            ),
            count=self.count,
        )
        return new_path

    def isDacAndFft(self):
        nodes = self.previous.split("-") if self.previous else []
        nodes.append(self.current)
        return "fft" in nodes and "dac" in nodes

    def isDacOnly(self):
        nodes = self.previous.split("-") if self.previous else []
        nodes.append(self.current)
        return "dac" in nodes and "fft" not in nodes

    def isFftOnly(self):
        nodes = self.previous.split("-") if self.previous else []
        nodes.append(self.current)
        return "fft" in nodes and "dac" not in nodes


# part 1
def get_config(lines):
    config = {}

    for line in lines:
        key = line[: line.index(":")]
        values = line[line.index(":") + 2 :].split(" ")
        config[key] = values
    return config


def move(config, path):
    if path.current == "out":
        return []
    result = []
    for nextPath in config[path.current]:
        result.append(path.move(nextPath))
    return result


def count_to_outs(config):
    paths = [PathToOut("you")]
    countToOut = 0
    while len(paths) > 0:
        paths = [result for path in paths for result in move(config, path)]
        countToOut = countToOut + len([path for path in paths if path.current == "out"])
    return countToOut


def is_good(path):
    if path.current != "out":
        return False

    return path.isDacAndFft()


def prune_paths(paths):
    categories = {"boring": {}, "dacOnly": {}, "fftOnly": {}, "both": {}}

    for path in paths:
        if path.isDacAndFft():
            category = categories["both"]
        elif path.isDacOnly():
            category = categories["dacOnly"]
        elif path.isFftOnly():
            category = categories["fftOnly"]
        else:
            category = categories["boring"]

        if path.current not in category:
            category[path.current] = path
        else:
            category[path.current].count += path.count

    return [path for category in categories.values() for path in category.values()]


def server_to_out(config):
    paths = [PathToOut("svr")]
    countToOut = 0
    while len(paths) > 0:
        paths = [result for path in paths for result in move(config, path)]
        paths = prune_paths(paths)
        countToOut = countToOut + sum([path.count for path in paths if is_good(path)])
    return countToOut
