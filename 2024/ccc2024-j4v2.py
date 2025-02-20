# CCC 2024 J4
# example translated from https://www.youtube.com/watch?v=vinLoGHIHjg

import string

# inputs
pressed = input()
displayed = input()

# stupidly long logic
if len(pressed) == len(displayed):
    for i in range(len(pressed)):
        if pressed[i] != displayed[i]:
            print("{} {}\n-".format(pressed[i], displayed[i]))
            quit()

for char in string.ascii_lowercase:
    louds = ""
    for char_p in pressed:
        if char_p != char:
            louds += char_p
    bads = ["", ""]
    works = True
    if len(louds) != len(displayed):
        continue
    for i in range(len(louds)):
        if louds[i] != displayed[i]:
            if not bads[0]:
                bads[0] = louds[i]
                bads[1] = displayed[i]
            elif bads[0] != louds[i]:
                works = False
                break
    if works:
        print("{} {}\n{}".format(bads[0], bads[1], char))