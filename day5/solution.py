stack1 = list("BSVZGPW")
stack2 = list("JVBCZF")
stack3 = list("VLMHNZDC")
stack4 = list("LDMZPFJB")
stack5 = list("VFCGJBQH")
stack6 = list("GFQTSLB")
stack7 = list("LGCZV")
stack8 = list("NLG")
stack9 = list("JFHC")

stacks = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]

with open("./input.txt") as file:
    for line in file:
        tokens = line.split(" ")
        amount = int(tokens[1])
        initialStackIndex = int(tokens[3]) - 1
        finalStackIndex = int(tokens[5]) - 1
        
        initialStack, finalStack = stacks[initialStackIndex], stacks[finalStackIndex]
        for i in range(amount) :
            if (initialStack):
                finalStack.append(initialStack.pop())

res = ""
for stack in stacks:
    res += stack.pop()

print(res)


stack1 = list("BSVZGPW")
stack2 = list("JVBCZF")
stack3 = list("VLMHNZDC")
stack4 = list("LDMZPFJB")
stack5 = list("VFCGJBQH")
stack6 = list("GFQTSLB")
stack7 = list("LGCZV")
stack8 = list("NLG")
stack9 = list("JFHC")

stacks = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]

with open("./input.txt") as file:
    for line in file:
        tokens = line.split(" ")
        amount = int(tokens[1])
        initialStackIndex = int(tokens[3]) - 1
        finalStackIndex = int(tokens[5]) - 1

        initialStack, finalStack = stacks[initialStackIndex], stacks[finalStackIndex]
        movedCrates = initialStack[-amount::]
        stacks[initialStackIndex] = initialStack[0:-amount]
        stacks[finalStackIndex] = finalStack + movedCrates

print(stacks)

res = ""
for stack in stacks:
    if (stack):
        res += stack.pop()

print(res)