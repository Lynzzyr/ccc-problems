players = int(input())
stars = []
stars_counter = 0

for i in range(players):
    stars.append(int(input()) * 5 - int(input()) * 3)

for i in stars:
    if (i > 40):
        stars_counter += 1

if (stars_counter == len(stars)):
    print(str(stars_counter) + "+")
else:
    print(stars_counter)