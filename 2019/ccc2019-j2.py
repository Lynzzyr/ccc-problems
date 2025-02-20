output = ""

for i in range(int(input())):

    usr_in = input().split()

    for j in range(int(usr_in[0])):

        output += usr_in[1]

    output += "\n"

print(output)