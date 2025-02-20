"""
CCC 2013 J3/S1

Problem Description
You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years
2014, 2015, 2016, 2017, 2018, 2019 each have distinct digits. 2012 does not have distinct digits,
since the digit 2 is repeated.
Given a year, what is the next year with distinct digits?

Input Specification
The input consists of one integer Y (0 ≤ Y ≤ 10000), representing the starting year.

Output Specification
The output will be the single integer D, which is the next year after Y with distinct digits.

Sample Input 1
1987

Output for Sample Input 1
2013

Sample Input 2
999

Output for Sample Input 2
1023
"""

# Inputs
y = int(input()) # init year

# Iterate
d = y + 1 # cannot start at y or else program will always output y

while True:
    iterate = ""

    for digit in str(d):
        if (digit not in iterate) : iterate += digit
    
    if (int(iterate) != d):
        d += 1
        continue
    else:
        break

# Final output
print(d)