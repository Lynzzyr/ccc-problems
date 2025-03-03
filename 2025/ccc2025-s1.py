# inputs
r = input().split()

A: int = int(r[0])
B: int = int(r[1])
X: int = int(r[2])
Y: int = int(r[3])

# process
p1 = 0 # stack below
p2 = 0 # stack to the side

w = 0 # left-right
l = 0 # up-down

# stack below
AX = sorted([A, X])
w = AX[-1]
l = B + Y
p1 = 2 * w + 2 * l

# stack to the side
w = A + X
BY = sorted([B, Y])
l = BY[-1]
p2 = 2 * w + 2 * l

# output
if p1 < p2:
    print(p1)
elif p2 < p1:
    print(p2)
else: # equal
    print(p1)