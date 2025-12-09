from dataclasses import dataclass, field
import heapq


@dataclass
class Box:
    id: str
    x: int
    y: int
    z: int


@dataclass
class Join:
    source: int
    dest: int
    dist: float


def build_boxes(lines: list):
    boxes = []
    id = 0
    for line in lines:
        bits = line.split(",")
        id = bits[0] + "-" + bits[1] + "-" + bits[2]
        boxes.append(Box(id, int(bits[0]), int(bits[1]), int(bits[2])))
    return boxes


# Part 1
def build_circuit(boxes: list, total: int):
    # Use a min-heap to efficiently track the shortest distances
    heap = []
    seen_pairs = set()

    for point in boxes:
        other_boxes = [p for p in boxes if p != point]
        for other in other_boxes:
            lower = min(point.id, other.id)
            upper = max(point.id, other.id)

            pair_key = (lower, upper)
            if pair_key in seen_pairs:
                continue

            seen_pairs.add(pair_key)
            distance = _distinceBetween(point, other)
            heapq.heappush(heap, (distance, lower, upper))

    # Extract the shortest 'total' joins
    shortest_joins = []
    for _ in range(min(total, len(heap))):
        dist, lower, upper = heapq.heappop(heap)
        shortest_joins.append(Join(lower, upper, dist))

    return shortest_joins


def part1(joins: list):

    circuits = []
    for join in joins:
        sourceCircuit = [circuit for circuit in circuits if join.source in circuit]
        destCircuit = [circuit for circuit in circuits if join.dest in circuit]

        if (
            len(sourceCircuit) > 0
            and len(destCircuit) > 0
            and sourceCircuit[0] == destCircuit[0]
        ):
            continue
        elif len(sourceCircuit) == 0 and len(destCircuit) == 0:
            newSet = set()
            newSet.add(join.source)
            newSet.add(join.dest)
            circuits.append(newSet)
        elif len(destCircuit) == 0 and len(sourceCircuit) > 0:
            sourceCircuit[0].add(join.dest)
        elif len(destCircuit) > 0 and len(sourceCircuit) == 0:
            destCircuit[0].add(join.source)
        else:
            sourceCircuit[0].update(destCircuit[0])
            circuits.remove(destCircuit[0])

    circuits.sort(key=lambda c: len(c), reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def part2(joins: list, boxes):

    # Initialise the circuits to the IDs of the boxes. Then it is jusdt merging if required
    circuits = [{box.id} for box in boxes]

    for join in joins:

        sourceCircuit = [circuit for circuit in circuits if join.source in circuit]
        destCircuit = [circuit for circuit in circuits if join.dest in circuit]

        if sourceCircuit[0] != destCircuit[0]:
            sourceCircuit[0].update(destCircuit[0])
            circuits.remove(destCircuit[0])

            if len(circuits) == 1:
                missing = [box.id for box in boxes if box.id not in circuits[0]]
                print(f"Missing box: {missing}")
                if len(circuits[0]) == len(boxes):
                    return int(join.source.split("-")[0]) * int(join.dest.split("-")[0])

    return 0


def _distinceBetween(a, b):
    return (((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z - b.z) ** 2)) ** 0.5
