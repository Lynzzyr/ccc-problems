import re

# inputs
S = input()
c = int(input())

# process
it = 0 # len of one iteration, NOT INDEX
r = [] # index of each repeated letter group

nums = re.findall(r"\d+", S)
for n in nums: it += int(n)

lets = re.findall(r"\D", S)
ind = 0 # amount to use next
for i in range(len(nums)):
    r.append(ind)
    ind += int(nums[i])

for i in range(len(r) - 1, -1, -1):
    pos = c % it
    if pos >= int(r[i]):
        print(lets[i])
        break