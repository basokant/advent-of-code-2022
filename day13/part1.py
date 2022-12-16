import json

with open("./input.txt") as file:
    lines = file.readlines()

def compare_data(left, right) :
    if (type(left) == type(right) == int):
        if (left < right) :
            return True
        elif (left > right) :
            return False

    elif (type(left) == type(right) == list):
        i = 0
        for i in range(min(len(left), len(right))):
            res = compare_data(left[i], right[i])
            if (res != None):
                return res

        if (len(left) < len(right)):
            return True
        elif (len(right) < len(left)):
            return False

    elif (type(left) == int and type(right) == list):
        return compare_data([left], right)

    elif (type(left) == list and type(right) == int):
        return compare_data(left, [right])

i = 0
res = 0
while i < len(lines):
    pair_num = i // 3 + 1
    print(f'== Pair {pair_num} ==')
    packet1 = json.loads(lines[i].strip())
    packet2 = json.loads(lines[i+1].strip())
    i += 3

    print(f'- Compare {packet1} vs {packet2}')
    bool = compare_data(packet1, packet2)
    print(bool)
    if (bool):
        res += pair_num

    print()

print(res)