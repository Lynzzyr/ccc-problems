digits = []

for j in range(4):
    digits.append(int(input()))

if (((digits[0] == 8) or (digits[0] == 9)) and ((digits[-1] == 8) or (digits[-1] == 9)) and (digits[1] == digits[2])):
    print("ignore")
else:
    print("answer")