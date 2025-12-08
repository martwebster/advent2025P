from dataclasses import dataclass, field


@dataclass
class Point:
    id: int
    x: int
    y: int
    z: int
    shortest: Point | None = None
    shortestDistance: float | None = None
    connex: list = field(default_factory=list)


# Part 1
def build_circuit(lines: list):
    points = []
    id = 0
    for line in lines:
        id = id + 1
        bits = line.split(",")
        points.append(Point(id, int(bits[0]), int(bits[1]), int(bits[2])))

    for point in points:
        other_points = [p for p in points if p != point]
        shortestDistance = None
        shortestPoint = None
        for other in other_points:
            distance = _distinceBetween(point, other)
            if shortestDistance == None or distance < shortestDistance:
                shortestDistance = distance
                shortestPoint = other
        point.shortest = shortestPoint
        point.shortestDistance = shortestDistance
    points.sort(key=lambda p: p.shortestDistance)

    for p in points:
        print(p.id, " connects to ", p.shortest.id, " distinace", p.shortestDistance)
    return points


def connect_points(points: list, total: int):
    print("here")
    count = 0
    for point in points:
        if count < total:
            source = point
            dest = point.shortest
            if dest not in source.connex and source not in dest.connex:
                source.connex.append(dest)
                dest.connex.append(source)
                count += 1


def build_circuits(points: list):
    connected_points = [point for point in points if point.connex != []]

    circuits = []
    while len(connected_points) > 0:
        point = connected_points.pop()
        circuit = set()
        circuit.add(point.id)
        queue = point.connex.copy()
        while len(queue) > 0:
            nextPoint = queue.pop()
            if nextPoint.id not in circuit:
                circuit.add(nextPoint.id)
                connected_points.remove(nextPoint)
                queue.extend(nextPoint.connex)
        circuits.append(circuit)

    circuits.sort(key=lambda c: len(c), reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def _distinceBetween(a: Point, b: Point):
    return (((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z - b.z) ** 2)) ** 0.5
