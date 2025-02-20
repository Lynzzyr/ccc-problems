# *x*
#  xx
# * *
line1 = ["*", "x", "*"]
line2 = [" ", "x", "x"]
line3 = ["*", " ", "*"]

k = int(input())
nline1 = ""
nline2 = ""
nline3 = ""

output = ""

# Add to nlines
for char in line1:
    for i in range(k):
        nline1 += char

for char in line2:
    for i in range(k):
        nline2 += char

for char in line3:
    for i in range(k):
        nline3 += char

# Add to output
for i in range(k):
    output += (nline1 + "\n")

for i in range(k):
    output += (nline2 + "\n")

for i in range(k):
    output += (nline3 + "\n")

print(output)