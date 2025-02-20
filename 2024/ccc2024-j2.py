# Inputs
D = int(input())

# Main logic
while True:
    curr_yobi = int(input())

    if curr_yobi >= D:
        break

    D += curr_yobi

# Output
print(D)