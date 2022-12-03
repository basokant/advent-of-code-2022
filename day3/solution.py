def item_priority(item_letter: str) -> int:
    if (ord(item_letter) >= ord('A') and ord(item_letter) <= ord('Z')):
        return ord(item_letter) - ord('A') + 27
    elif (ord(item_letter) >= ord('a') and ord(item_letter) <= ord('z')):
        return ord(item_letter) - ord('a') + 1

# print(item_priority('a'))
# print(item_priority('z'))
# print(item_priority('A'))
# print(item_priority('Z'))

def get_common_item(items1: str, items2: str) -> str:
    for item in items1:
        if item in items2:
            return item
    return None

def sum_of_item_priority(items: str) -> int:
    sum = 0
    for item in items:
        sum += item_priority(item)
    return sum

def get_common_items(file_path: str) -> int:
    common_items = list()

    with open(file_path) as file:
        for line in file:
            first, second = line[:len(line) // 2], line[len(line) // 2:]

            common_item = get_common_item(first, second)
            if (common_item):
                common_items.append(common_item)
    
    return common_items

def get_total_rusksack_priorities(file_path: str) -> int:
    common_items = get_common_items(file_path)
    return sum_of_item_priority(common_items)

print(get_total_rusksack_priorities("./test.txt"))
print(get_total_rusksack_priorities("./input.txt"))

def get_badge(elf1_rusksack: str, elf2_rusksack: str, elf3_rusksack: str) -> str:
    for item in elf1_rusksack:
        if item in elf2_rusksack and item in elf3_rusksack:
            return item
    return None

def get_badges(file_path: str) -> int:
    badges = list()

    group = list()
    with open(file_path) as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            group = [lines[i], lines[i + 1], lines[i + 2]]
            badge = get_badge(group[0], group[1], group[2])
            if (badge):
                badges.append(badge)
    
    return badges

def get_total_badge_priorities(file_path: str) -> int:
    badges = get_badges(file_path)
    return sum_of_item_priority(badges)

print(get_total_badge_priorities("./test.txt"))
print(get_total_badge_priorities("./input.txt"))