# samples
"""
3
3 1 2
3 1 1
YES
1
R 1 2

4
1 2 4 3
1 4 2 3
NO

4
2 1 4 3
2 1 4 3
YES
0

15
4 7 4 3 2 4 8 7 9 2 9 0 3 4 2
4 7 4 3 3 3 3 9 9 2 9 0 3 2 2
YES
3
R 3 6
L 7 8
L 13 14

11
9 4 3 5 6 1 1 1 1 4 3
9 4 5 5 5 5 5 1 1 4 3
YES
2
L 2 3
R 2 6

8
1 4 3 6 1 9 0 3
1 4 3 4 4 4 0 3
NO

8
6 5 7 4 8 3 3 4
6 6 6 6 6 3 3 3
YES
2
R 0 4
R 6 7

8
4 9 3 8 3 0 1 5
4 3 3 8 8 1 1 5
YES
3
L 1 2
R 3 4
L 5 6
"""

import re

# inputs
N = int(input())

A = ""
B = ""

AIn = input()
for char in AIn:
    if char != " ":
        A += char
Bin = input()
for char in Bin:
    if char != " ":
        B += char

"""
2 passes
first find repeated groups in B
second find which are irrelevant (also occurs as A)
-> result is start and end indices of swiped groups

for each group check if within indices of group has digit of group in A
-> if all swiped groups do then YES, if not NO

if digit of group in A present
- in either left or right edge: group was formed from 1 swipe
- in anywhere else (the middle): group was formed from 2 swipes
-> count total and this is second output as integer

if digit of group in A present
- in left edge: start of swipe from left bound to right bound
- in right edge: start of swipe from right bound to left bound
- in anywhere else (the middle): start of swipe from digit index to left bound, to right bound
"""
# logic
bGroups = []

# find repeated groups in passes, elim irrelevant; inclusive end index
aGroups = [ (match.start(), match.end() - 1, match[0]) for match in re.finditer(r"(\d)(\1+)", A) ]
bTemp = [ (match.start(), match.end() - 1, match[0]) for match in re.finditer(r"(\d)(\1+)", B) ]

for bg in bTemp:
    # print(b_g)
    if A.find(bg[2], bg[0]) == -1:
        bGroups.append(bg)

# print(b_groups)

# check if swipe is possible, if digit is in A; count and print swipes
# each tuple in b_groups (start: int, end: int, val_group: str)
yes = "NO"
count = 0
swipes = []

if ( bGroups == [] and A == B ):
    yes = "YES"
else:
    for bg in bGroups:
        # exclusive end index for find()
        find = A.find(bg[2][0], bg[0], bg[1] + 1)
        # print("b_g[2]: %s" % b_g[2][0])
        # print(find)
        # outside group
        if find == -1:
            yes = "NO"
            break
        # on left group edge
        elif find == bg[0]:
            yes = "YES"
            count += 1
            swipes.append(f"R {bg[0]} {bg[1]}")
        # on right group edge
        elif find == bg[1]:
            yes = "YES"
            count += 1
            swipes.append(f"L {bg[0]} {bg[1]}")
        # in group middle
        else:
            yes = "YES"
            count += 2
            swipes.append(f"L {bg[0]} {find}")
            swipes.append(f"R {bg[0]} {bg[1]}")

# final output
print(yes)
if yes == "YES": print(count)
if swipes:
    for swipe in swipes: print(swipe)