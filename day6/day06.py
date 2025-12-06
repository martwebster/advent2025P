# Part 1
def total_maths(lines: list):

    rows = []
    for line in lines:
        chunks = line.split(" ")
        chunks = [chunk for chunk in chunks if chunk != ""]
        rows.append(chunks)

    sums = []
    for col in range(0, len(rows[0])):
        sum = []
        for row in rows:
            sum.append(row[col])
        sums.append(sum)

    total = 0
    for sum in sums:
        operators = sum[:-1]
        sumTotal = int(operators[0])
        if sum[-1] == "+":
            for part in operators[1:]:
                sumTotal = sumTotal + int(part)
        else:
            for part in operators[1:]:
                sumTotal = sumTotal * int(part)
        total = total + sumTotal
    return total


def part_2(lines: list, cols: list):

    sums = [[line[col[0] : col[1]] for line in lines] for col in cols]

    total = 0
    for sum in sums:
        operators = sum[:-1]
        sumTotal = 0
        for colIndex in range(len(sum[0])):
            num = [operator[colIndex] for operator in operators]
            num = int("".join(num))
            if sum[-1][0] == "+":
                sumTotal += num
            else:
                sumTotal = num if sumTotal == 0 else sumTotal * num
        total = total + sumTotal
    return total


def getCoumnDefs(operatorLine):
    columns = []
    start = 0
    for index, char in enumerate(operatorLine):
        if char in "+*":
            if index > 0:
                columns.append([start, index - 1])
                start = index
    columns.append([start, len(operatorLine)])
    return columns
