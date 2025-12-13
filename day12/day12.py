def get_present_count(data):
    all_lines = [x.splitlines() for x in data.split("\n\n")]
    present_areas = all_lines[-1:][0]
    count = 0
    for present_area in present_areas:
        x = int(present_area[0 : present_area.index("x")])
        y = int(present_area[present_area.index("x") + 1 : present_area.index(":")])
        required_area = x * y

        present_counts = [
            int(x) for x in present_area[present_area.index(": ") + 2 :].split(" ")
        ]
        total_area = 9 * sum(present_counts)
        if required_area >= total_area:
            count = count + 1
    return count
