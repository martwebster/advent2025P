def get_password(data):
    pos = 50
    password_count = 0
    
    for direction in data:
        step = int(direction[1:]) % 100
        
        if direction[0] == "L":
            pos -= step
        elif direction[0] == "R":
            pos += step
        
        # Wrap position within 0-99 range
        pos = pos % 100
        
        if pos == 0:
            password_count += 1
    
    return password_count


def get_password2(data):
    pos = 50
    password_count = 0
    
    for direction in data:
        step = int(direction[1:])
        move = -1 if direction[0] == "L" else 1
        
        for _ in range(step):
            pos = (pos + move) % 100
            
            if pos == 0:
                password_count += 1
    
    return password_count


if __name__ == "__main__":
    # Read the actual puzzle input
    with open("day1/part1.txt", "r") as f:
        puzzle_input = f.read().strip()

    directions = puzzle_input.splitlines()

    # Solve both parts
    part1_answer = get_password(directions)
    part2_answer = get_password2(directions)

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")
