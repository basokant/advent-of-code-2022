global cycle_num
cycle_num = 1

global X
X = 1

global signal_strengths
signal_strengths = list()

with open("./input.txt") as file :
    instructions = [instruction.strip().split(' ') for instruction in file.readlines()]

instruction_num = 0

def increment_cycle() :
    global cycle_num
    if (cycle_num - 20) % 40 == 0 :
        print(cycle_num)
        curr_signal_strength = cycle_num * X
        signal_strengths.append(curr_signal_strength)

    cycle_num += 1

while(cycle_num <= 220) :
    if (instruction_num in range(len(instructions))) :
        instruction = instructions[instruction_num]
        op_code = instruction[0]

        if op_code == "addx" :
            value = int(instruction[1])
            increment_cycle()
            increment_cycle()
            X += value
        else :
            increment_cycle()
        
        instruction_num += 1
    else :
        increment_cycle()

print(signal_strengths)
print("Sum of Signal Strengths:", sum(signal_strengths))