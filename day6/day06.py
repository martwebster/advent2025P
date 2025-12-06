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
        operands = [int(x) for x in sum[:-1]]
        operator = sum[-1]
        sumTotal = operands[0]
        for operand in operands[1:]:
            if operator == "+":
                sumTotal = sumTotal + operand
            else:
                sumTotal = sumTotal * operand
        total = total + sumTotal
    return total


def part_2(lines: list):

    max_line_length = max(len(line) for line in lines)
    operator_line = lines[-1].ljust(max_line_length)
    col_definitions = _build_column_definitions(operator_line)

    sums = [[line[col[0] : col[1]] for line in lines] for col in col_definitions]
    return sum(_calculateColumnSum(sum) for sum in sums)


def _build_column_definitions(operatorLine):
    columns = []
    start = 0
    for index, char in enumerate(operatorLine):
        if char in "+*":
            if index > 0:
                columns.append([start, index - 1])
                start = index
    columns.append([start, len(operatorLine)])
    return columns


def _calculateColumnSum(sum: list):
    operands, operator = sum[:-1], sum[-1][0]
    total = 0
    for colIndex in range(len(sum[0])):
        digits = [operand[colIndex] for operand in operands]
        num = int("".join(digits))
        if operator == "+":
            total += num
        else:
            total = num if total == 0 else total * num
    return total
