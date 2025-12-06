def count_fresh(freshList: list, ingredients: list):
    fresh_count = 0
    for ingredient in ingredients:
        if _isFresh(int(ingredient), freshList):
            fresh_count = fresh_count + 1
    return fresh_count


def _isFresh(ingredient: int, freshList: list):
    for fresh in freshList:
        range_from = int(fresh.split("-")[0])
        range_to = int(fresh.split("-")[1])

        if ingredient <= range_to and ingredient >= range_from:
            return True

    return False


# Part 2
def get_range(freshList: list):
    # Convert list to list of ranges
    fresh_ranges = [
        [int(fresh.split("-")[0]), int(fresh.split("-")[1])] for fresh in freshList
    ]
    fresh_ranges.sort(key=lambda x: x[0])

    result = []
    for fresh in fresh_ranges:
        if not _merge(result, fresh):
            result.append(fresh)

    return _calculate_total(result)


def _merge(source_ranges, range):
    for source in source_ranges:
        if range[0] >= source[0] and range[1] <= source[1]:
            return True
        if (range[0] >= source[0] and range[0] <= source[1]) or (
            range[1] >= source[0] and range[1] <= source[1]
        ):
            source[0] = min(source[0], range[0])
            source[1] = max(source[1], range[1])
            return True
    return False


def _calculate_total(fresh_ranges: list):
    total = 0
    for fresh in fresh_ranges:
        total = total + (fresh[1] - fresh[0]) + 1

    return total
