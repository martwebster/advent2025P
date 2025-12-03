def getJoltage(data, length=2):
    int_array = [int(x) for x in data]

    result = ""
    left_to_find = length
    while left_to_find > 0:
        if left_to_find > 1:
            found = max(int_array[: -(left_to_find - 1)])
        else:
            found = max(int_array)
        result += str(found)
        left_to_find = left_to_find - 1

        # truncate the array to be ready for
        int_array = int_array[int_array.index(found) + 1 :]

    print(result)
    return int(result)


def getTotalVolage(banks, length=2):
    return sum(getJoltage(bank, length) for bank in banks.splitlines())
