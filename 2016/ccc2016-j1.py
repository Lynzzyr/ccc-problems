stats = ""
for j in range(6):
    stats += input()

if (stats.count("W") >= 5):
    print(1)
elif (3 <= stats.count("W") <= 4):
    print(2)
elif (1 <= stats.count("W") <= 2):
    print(3)
elif (stats.count("W") == 0):
    print(-1)