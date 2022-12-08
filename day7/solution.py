from collections import defaultdict

MAX_SIZE = 100000
DISK_SPACE = 70000000
REQUIRED_SPACE = 30000000

with open("./input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

directory_sizes = defaultdict(int)
directory_stack = list()

for line in lines :
    match line.split():
        case ["$", _, ".."]:
            directory_stack.pop()
        case ["$", _, dir]:
            directory_stack.append(dir)
        case [file_size, _] if file_size.isdigit():
            for i in range(len(directory_stack) + 1):
                path = "/" + "/".join(directory_stack[:i])
                directory_sizes[path] += int(file_size)

print(sum(filter(lambda size: size <= MAX_SIZE, directory_sizes.values())))

unused_space = DISK_SPACE - directory_sizes['/']
needed_space = REQUIRED_SPACE - unused_space

print(min(filter(lambda size: size >= needed_space, directory_sizes.values())))