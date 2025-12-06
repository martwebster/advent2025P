def get_invalidIds(data):
    ids_to_check = data.split(",")
    total = 0
    for id in ids_to_check:
        total += _isInvalid(id)

    return total


def _isInvalid(item):
    start = int(item.split("-")[0])
    end = int(item.split("-")[1])

    total = 0

    for num in range(start, end + 1):
        size = len(str(num))
        first = str(num)[0 : size // 2]
        second = str(num)[size // 2 :]

        if first == second:
            print(f"Size: {size}, First: {first}, Second: {second}")
            total += num

    return total


def get_invalidIds2(productIds):
    # Same as a map statement
    # return sum(_invalid_product_id(id) for id in productIds.split(","))
    return sum(map(_invalid_product_id, productIds.split(",")))


def _invalid_product_id(item: str) -> int:

    item.split("")

    start = int(item.split("-")[0])
    end = int(item.split("-")[1])

    total = 0
    for num in range(start, end + 1):
        size = len(str(num))
        good = False
        for digits in range(1, size):
            to_check = str(num)[0:digits]
            count = str(num).count(to_check)
            expected = len(str(num)) / digits
            if count == expected:
                if count > 1:
                    good = True
                    print(f" {to_check}  {count} times in {num}")
        if good:
            total = total + num

    return total
