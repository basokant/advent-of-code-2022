from operator import add, sub

def add_positions(pos1, pos2) :
    return list(map(add, pos1, pos2))

def sub_positions(pos1, pos2) :
    return list(map(sub, pos1, pos2))

def get_magnitude(pos) :
    return abs(pos[0]**2 + pos[1]**2) ** 0.5

with open("./input.txt") as file:
    # converts the moves from the file into a list of tuples (direction (char), num steps (int))
    motions = [[line.split()[0], int(line.split()[1])] for line in file.readlines()]

head_pos, tail_pos = [0,0], [0,0]
tail_positions = set()

tail_positions.add(tuple(tail_pos))

print(head_pos, tail_pos)

for motion in motions :
    print(motion)
    direction, magnitude = motion[0], motion[1]

    match direction:
        case "R":
            head_displacement = [1, 0]
        case "L":
            head_displacement = [-1, 0]
        case "U":
            head_displacement = [0, 1]
        case "D":
            head_displacement = [0, -1]

    for step in range(magnitude) :
        old_head_pos = head_pos
        head_pos = add_positions(head_pos, head_displacement)

        # are the head and tail still touching?
        head_tail_displacement = sub_positions(head_pos, tail_pos)
        radius = get_magnitude(head_tail_displacement)
        if (radius > (2 ** 0.5)) :
            tail_pos = old_head_pos

        print(head_pos, tail_pos)
        tail_positions.add(tuple(tail_pos))

print(tail_positions)
print(len(tail_positions))