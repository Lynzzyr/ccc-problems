# inputs
N = int(input())

H = []
for i in range(N):
    H.append(int(input()))

# logic
hats = 0
for i in range(int(N / 2)):
    if H[i] == H[int(len(H) / 2)]:
        hats += 1
for i in range(int(N / 2), N):
    if H[i] == H[int(len(H) /2) + i - 1]:
        hats += 1

print(hats)