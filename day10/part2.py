cycle_num = 1
X = 1

global signal_strengths
signal_strengths = list()

crt = [['.'] * 40 for i in range(6)]

with open("./input.txt") as file :
    instructions = [instruction.strip().split(' ') for instruction in file.readlines()]

instruction_num = 0

def run_cycle() :
    global cycle_num
    global crt

    if (cycle_num - 20) % 40 == 0 :
        print(cycle_num)
        curr_signal_strength = cycle_num * X
        signal_strengths.append(curr_signal_strength)

    crt_row_num = (cycle_num - 1) // 40
    pixel_num = (cycle_num - 1) % 40

    if (X - 1 <= pixel_num and pixel_num <= X + 1) :
        crt[crt_row_num][pixel_num] = '#'
    
    print("Cycle_num: %d, Row_num: %d, Pixel_num: %d, Sprite_Position: %d, Pixel: %s" % (cycle_num, crt_row_num, pixel_num, X, crt[crt_row_num][pixel_num]))

    cycle_num += 1

def render_image(crt):
    for row in crt :
        for pixel in row :
            print(pixel, end='')
        print()

while(cycle_num <= 240) :
    if (instruction_num in range(len(instructions))) :
        instruction = instructions[instruction_num]
        op_code = instruction[0]

        if op_code == "addx" :
            value = int(instruction[1])
            run_cycle()
            run_cycle()
            X += value
        else :
            run_cycle()
        
        instruction_num += 1
    else :
        run_cycle()

print(signal_strengths)
print("Sum of Signal Strengths:", sum(signal_strengths))

print(crt)
render_image(crt)