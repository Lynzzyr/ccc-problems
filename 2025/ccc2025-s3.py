# SUBTASK 1 ONLY: Q = 0 ALWAYS

# globals
N: int = 0
M: int = 0
Q: int = 0
pens: dict = {}

# inputs
r1 = input().split()
N = int(r1[0])
M = int(r1[1])
Q = int(r1[2])

for i in range(N):
    rl = input().split()
    if int(rl[0]) not in list(pens.keys()):
        pens.update({int(rl[0]): [ int(rl[1]) ]})
    else:
        tl1: list = pens.get(int(rl[0]))
        tl1.append(int(rl[1]))
        pens.update({int(rl[0]): sorted(tl1)})

# process
rep = [] # color, prettiness to replace with
cols = list(pens.keys())
for c in cols:
    cos = cols
    cos.remove(c)
    ph = pens.get(c)[-1] # highest prettiness
    for co in cos:
        ls = pens.get(co)
        for i in range(len(ls) - 1): # skip last value as it will never be avail
            if ls[i] > ph and ls[i] != rep:
                rep.clear()
                rep.append(c)
                rep.append(co)
                rep.append(ls[i])
                break

# print(rep)

if rep:
    tl2: list = pens.get(rep[1])
    tl2.remove(rep[2])
    pens.update({rep[1]: tl2})

    tl3: list = pens.get(rep[0])
    tl3.append(rep[2])
    pens.update({rep[0]: tl3})
else: pass

# output
tp = 0
for c in list(pens.keys()):
    tp += pens.get(c)[-1]
print(tp)