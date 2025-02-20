import re

# inputs
l1 = input().split()

T = int(l1[0])
N = int(l1[1])

s = []

for i in range(T):
    s.append(input())

# logic
for l in s:
    checked = []
    heavy = []
    for char in l:
        if char in checked:
            continue
        ln = len(re.findall(char, l))
        if ln > 1:
            heavy.append(char)
        checked.append(char)

    out ="T"
    if l[0] in heavy:
        try:
            for i in range(0, N, 2):
                if l[i] not in heavy:
                    out = "F"
                    break
        except IndexError: pass
        try:
            for i in range(1, N, 2):
                if l[i] in heavy:
                    out = "F"
                    break
        except IndexError: pass
    else:
        try:
            for i in range(1, N, 2):
                if l[i] not in heavy:
                    out = "F"
                    break
        except IndexError: pass
        try:
            for i in range(0, N, 2):
                if l[i] in heavy:
                    out = "F"
                    break
        except IndexError: pass
    
    print(out)