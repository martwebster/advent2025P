from dataclasses import dataclass


@dataclass
class Pos:
    x: int
    y: int

    def adjacent_positions(self):
        return [
            Pos(self.x - 1, self.y - 1),
            Pos(self.x, self.y - 1),
            Pos(self.x + 1, self.y - 1),
            Pos(self.x - 1, self.y),
            Pos(self.x + 1, self.y),
            Pos(self.x - 1, self.y + 1),
            Pos(self.x, self.y + 1),
            Pos(self.x + 1, self.y + 1),
        ]


def _is_paper(grid, pos):
    # Return false if out of bounds
    if pos.y < 0 or pos.x < 0 or pos.y >= len(grid) or pos.x >= len(grid[0]):
        return False
    return grid[pos.y][pos.x] == "@"


def _can_access(grid, cell):
    papers = 0
    for adjacent in cell.adjacent_positions():
        if _is_paper(grid, adjacent):
            papers += 1
    if papers < 4:
        return True
    return False


# Part 1 - Count the rolls that can be accessed
def count_accessable_rolls(grid):
    return len(get_accessable_rolls(grid))


def get_accessable_rolls(grid):
    access_count = []
    for y in range(len(grid)):
        print("")
        for x in range(len(grid[y])):
            cell = grid[y][x]
            if cell == "@" and _can_access(grid, Pos(x, y)):
                access_count.append(Pos(x, y))
                print("x", end="")
            else:
                print(cell, end="")
    print()
    return access_count


def remove_rolls(grid):
    rolls = get_accessable_rolls(grid)
    print(len(rolls), "rolls of paper")
    for roll in rolls:
        grid[roll.y] = grid[roll.y][: roll.x] + "." + grid[roll.y][roll.x + 1 :]
    return len(rolls)


# Part2
def remove_all_rolls(data):
    removing = remove_rolls(data)
    total_removed = removing
    while removing > 0:
        removing = remove_rolls(data)
        total_removed += removing
    return total_removed
