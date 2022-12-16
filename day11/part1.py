class Monkey:
    monkeys = list()

    def __init__(self, starting_items, operation_str, test_num, monkey_true, monkey_false) :
        self.items = starting_items
        self.num_inspected_items = 0
        self.operation_str = operation_str
        self.test_num = test_num
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false

        self.monkeys.append(self)

    def operation(self, item_index) :
        item = self.items[item_index]
        tokens = self.operation_str.split()
        if (tokens[0] == 'old') :
            tokens[0] = str(item)
        
        if (tokens[2] == 'old') :
            tokens[2] = str(item)

        new = eval("".join(tokens))
        self.items[item_index] = new

    def throw_item(self, item, monkey_num) :
        recieving_monkey = self.monkeys[monkey_num]
        recieving_monkey.items.append(item)

    def inspect_items(self) :
        for i in range(len(self.items)) :
            self.num_inspected_items += 1
            self.operation(i)
            self.items[i] //= 3
        
        items_copy = self.items.copy()
        
        for item in items_copy :
            item_index = self.items.index(item)
            new_item = self.items.pop(item_index)
            # decide which monkey to throw the item to
            if (new_item % self.test_num == 0) :
                self.throw_item(new_item, self.monkey_true)
            else :
                self.throw_item(new_item, self.monkey_false)

    def round(self) :
        for monkey in self.monkeys :
            monkey.inspect_items()

    def run(self, num_rounds) :
        for i in range(num_rounds) :
            self.round()

    def get_monkey_business(self) :
        total_inspected_items = sorted([monkey.num_inspected_items for monkey in self.monkeys])
        return total_inspected_items[-1] * total_inspected_items[-2]

with open('./input.txt') as file :
    lines = [line.strip().split() for line in file.readlines()]

print(lines)
monkey_line_nums = [i for i in range(len(lines)) if len(lines[i]) > 0 and lines[i][0] == 'Monkey']
print(monkey_line_nums)
monkeys = list()

for monkey_line_num in monkey_line_nums :
    starting_items = [int(item.split(',')[0]) for item in lines[monkey_line_num + 1][2:]]
    operation_str = " ".join(lines[monkey_line_num + 2][3:]).strip()
    test_num = int(lines[monkey_line_num + 3][3])
    monkey_true = int(lines[monkey_line_num + 4][5])
    monkey_false = int(lines[monkey_line_num + 5][5])

    monkey = Monkey(starting_items, operation_str, test_num, monkey_true, monkey_false)
    monkeys.append(monkey)

monkeys[0].run(20)
monkey_business = monkeys[0].get_monkey_business()
print(monkey_business)