# inputs
N = int(input())
H = []
for i in range(N):
    H.append(int(input()))

out = 0

# logic
for i in range(N // 2):
    if H[i] == H[i + (N // 2)]:
        out += 1
for i in range(N // 2, N, 1):
    if H[i] == H[i - (N // 2)]:
        out += 1

print(out)