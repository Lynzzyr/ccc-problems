appl_scores = []
for j in range(3):
    appl_scores.append(int(input()))
bnn_scores = []
for j in range(3):
    bnn_scores.append(int(input()))

appl = appl_scores[0] * 3 + appl_scores[1] * 2 + appl_scores[2]
bnn = bnn_scores[0] * 3 + bnn_scores[1] * 2 + bnn_scores[2]

if (appl > bnn):
    print("A")
elif (bnn > appl):
    print("B")
else:
    print("T")