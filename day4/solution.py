def are_sections_fully_contained(section_range1, section_range2) -> bool:
    res = section_range1[0] >= section_range2[0] and section_range1[1] <= section_range2[1]
    res = res or (section_range2[0] >= section_range1[0] and section_range2[1] <= section_range1[1])

    return res

print(are_sections_fully_contained((2,8), (3,7)))

def get_section_range(line):
    lower, upper = line.split("-")
    return (int(lower), int(upper))

def get_pairings(file_path):
    pairings = []
    with open(file_path) as file:
        for line in file:
            elf1, elf2 = line.split(",")
            elf1_sections = get_section_range(elf1)
            elf2_sections = get_section_range(elf2)

            pairings.append((elf1_sections, elf2_sections))

    return pairings

def num_sections_fully_contained(file_path: str) -> int :
    pairings = get_pairings(file_path)
    num_contained = 0
    for pair in pairings:
        if are_sections_fully_contained(pair[0], pair[1]):
            num_contained += 1

    return num_contained

print(num_sections_fully_contained("./test.txt"))
print(num_sections_fully_contained("./input.txt"))

def are_sections_overlapping(section_range1, section_range2) -> bool:
    return section_range1[0] <= section_range2[1] and section_range2[0] <= section_range1[1]

def num_sections_overlapping(file_path: str) -> int :
    pairings = get_pairings(file_path)
    num_overlapping = 0
    for pair in pairings:
        if are_sections_overlapping(pair[0], pair[1]):
            num_overlapping += 1

    return num_overlapping

print(num_sections_overlapping("./test.txt"))
print(num_sections_overlapping("./input.txt"))