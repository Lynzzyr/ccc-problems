coord1 = int(input())
coord2 = int(input())
quadrant = 0

if (coord1 > 0 and coord2 > 0):
    quadrant = 1
elif (coord1 < 0 and coord2 > 0):
    quadrant = 2
elif (coord1 < 0 and coord2 < 0):
    quadrant = 3
elif (coord1 > 0 and coord2 < 0):
    quadrant = 4

print(quadrant)