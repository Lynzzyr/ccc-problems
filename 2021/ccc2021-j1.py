degc = int(input())
kpa = 5 * degc - 400

print(kpa)
if (100 - kpa > 0):
    print(1)
elif (100 - kpa < 0):
    print(-1)
else:
    print(0)