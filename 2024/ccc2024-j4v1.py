# N ≤ 50

# Inputs
keys = input()
displays = input()

# Main logic
silly = ("", "")
quiet = ""

k = 0
d = 0

while True:
    if k == len(keys) - 1:
        break

    try:
        if keys[k] == displays[d] or (keys[k] == silly[0] and displays[d] == silly[1]):
            k += 1
            d += 1
            continue
    except IndexError:
        quiet = keys[k]
        break

    if keys[k + 1] == displays[d + 1]:
        silly = (keys[k], displays[d])
        k += 1
        d += 1
    elif keys[k + 1] == displays[d] or (keys[k + 1] == silly[0] and displays[d] == silly[1]):
        quiet = keys[k]
        k += 1

# Output
print(silly[0], silly[1])

if quiet == "":
    print("-")
else:
    print(quiet)