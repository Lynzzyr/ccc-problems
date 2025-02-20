# Inputs
scores = []

for i in range(int(input())):
    scores.append(int(input()))

scores = sorted(scores, reverse = True)

# Main logic
bronze_score = scores[0]
count = 0
for score in scores:
    if count == 2:
        break

    if score < bronze_score:
        bronze_score = score
        count += 1

# Output
print(bronze_score, scores.count(bronze_score))