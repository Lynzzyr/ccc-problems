init_input = input()
instructions = []
prev_end = 0

for j in range(len(init_input)):
    if (init_input[j].isnumeric()):
        if (j + 1 < len(init_input)):
            if (not init_input[j + 1].isnumeric()):
                instructions.append(init_input[prev_end:j + 1])
                prev_end = j + 1
        elif (j + 1 == len(init_input)):
            instructions.append(init_input[prev_end:j + 1])

for j in range(len(instructions)):
    print(instructions[j].replace("+", " tighten ").replace("-", " loosen "))