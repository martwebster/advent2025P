def isPaper(data, x, y):
    if y < 0:
        return False
    if x < 0:
        return False
    if x >= len(data[0]):
        return False
    if y >= len(data):
        return False
    return data[y][x] == "@"


def canAccess(data, x, y):
    papers = [
        isPaper(data, x - 1, y - 1),
        isPaper(data, x, y - 1),
        isPaper(data, x + 1, y - 1),
        isPaper(data, x - 1, y),
        isPaper(data, x + 1, y),
        isPaper(data, x - 1, y + 1),
        isPaper(data, x, y + 1),
        isPaper(data, x + 1, y + 1),
    ]
    if papers.count(True) < 4:
        return True

    return False


def get_positions(data):
    access_count = 0
    for y in range(len(data)):
        print("")
        for x in range(len(data[y])):
            cell = data[y][x]
            if cell == "@" and canAccess(data, x, y):
                access_count = access_count + 1
                print("x", end="")
            else:
                print(cell, end="")
    return access_count


def remove_rolls(data):
    access_count = []
    for y in range(len(data)):
        print("")
        for x in range(len(data[y])):
            cell = data[y][x]
            if cell == "@" and canAccess(data, x, y):
                access_count.append([x, y])
                print("x", end="")
            else:
                print(cell, end="")

    print()
    print(len(access_count), "rolls of paper")
    for item in access_count:
        y = item[1]
        x = item[0]
        data[y] = data[y][:x] + "." + data[y][x + 1 :]
    return len(access_count)


def remove_all_rolls(data):
    count = remove_rolls(data)
    total = count
    while count > 0:
        count = remove_rolls(data)
        total = total + count
    return total
