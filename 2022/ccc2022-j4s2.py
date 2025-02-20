# Global objects
violations = 0

pairs = []
for j in range(int(input())):
    pairs.append(input())

segregations = []
for j in range(int(input())):
    segregations.append(input())

groups = []
for j in range(int(input())):
    groups.append(" " + input() + " ")

# Test for pairs in groups, tests if only one OR neither name(s) from pair is present, adds a violation if all groups pass test
for j in range(len(pairs)):
    test_count = 0
    temp_list = pairs[j].split()

    for i in range(len(groups)):
        if ( ( (" " + temp_list[0] + " ") in groups[i]) ^ ( (" " + temp_list[1] + " ") in groups[i]) ) or ( (" " + temp_list[0] + " ") not in groups[i]) & ( (" " + temp_list[1] + " ") not in groups[i]):
            test_count += 1
    
    if (test_count == len(groups)):
        violations += 1

# Test for segregations in groups, tests if only both names from segregation are present, adds a violation if both names found in group
for j in range(len(segregations)):
    test_count = 0
    temp_list = segregations[j].split()

    for i in range(len(groups)):
        if ( (" " + temp_list[0] + " ") in groups[i]) & ( (" " + temp_list[1] + " ") in groups[i]):
            test_count += 1
    
    if (test_count == 1):
        violations += 1

# Final output
print(violations)