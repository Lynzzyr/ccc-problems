n = int(input())
lines = []
for i in range(n):
    lines.append(input())

days = []
for i in range(5):
    curr_el = ""

    for j in range(n):
        curr_el += lines[j][i]
    
    days.append(curr_el)

occurs = []
for i in range(5):
    occurs.append(days[i].count("Y"))

max_num = 0
for i in occurs:
    if (i > max_num):
        max_num = i

indexes = []
counter = 0
for i in occurs:
    if (i == max_num):
        indexes.append(occurs.index(i, counter) + 1)

    counter += 1

if (len(indexes) > 1):
    for i in range(len(indexes)):
        if (i + 1 == len(indexes)):
            print(indexes[i])
        else:
            print(indexes[i], end = ",")
else:
    print(indexes[0])