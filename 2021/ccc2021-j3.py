in_nums = []
in_bool = True
prev_dir = ""
while (in_bool == True):
    curr_in = input()
    if (int(curr_in) == 99999):
        in_bool = False
    else:
        in_nums.append(curr_in)

for j in range(len(in_nums)):
    if ((int(in_nums[j][0]) + int(in_nums[j][1])) % 2 == 0):
        print("right {}".format(in_nums[j][2:5]))
        prev_num = "right"
    elif (in_nums[j][0:1] == "00"):
        print(prev_dir + in_nums[j][2:5])
    else:
        print("left {}".format(in_nums[j][2:5]))