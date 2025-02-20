ccc_date = [2, 18]
in_date = []

for j in range(2):
    in_date.append(int(input()))

if (in_date[0] < ccc_date[0]):
    print("Before")
elif (in_date[0] > ccc_date[0]):
    print("After")
elif (in_date[1] < ccc_date[1]):
    print("Before")
elif (in_date[1] > ccc_date[1]):
    print("After")
else:
    print("Special")