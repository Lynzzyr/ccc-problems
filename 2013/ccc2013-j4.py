"""
CCC 2013 J4

Problem Description
You have been asked by a parental unit to do your chores.

Each chore takes a certain amount of time, but you may not have enough time to do all of your
chores, since you can only complete one chore at a time. You can do the chores in any order that
you wish.

What is the largest amount of chores you can complete in the given amount of time?

Input Specification
The first line of input consists of an integer T (0 ≤ T ≤ 100000), which is the total number of
minutes you have available to complete your chores.

The second line of input consists of an integer C (0 ≤ C ≤ 100), which is the total number
of chores that you may choose from. The next C lines contain the (positive integer) number of
minutes required to do each of these chores. You can assume that each chore will take at most
100000 minutes.

Output Specification
The output will be the maximum number of chores that can be completed in time T.

Sample Input 1
6
3
3
6
3

Output for Sample Input 1
2

Explanation of Output for Sample Input 1
Chores must be completed in at most 6 minutes. There are 3 chores available. The first chore takes
3 minutes. The second chore takes 6 minutes. The third chore takes 3 minutes. The answer is
2 since only 2 of these chores can be completed in 6 minutes of time. Specifically, the first and
last chore can be completed in the allowable time. It is not possible to complete all 3 chores in 6
minutes.

Sample Input 2
6
5
5
4
3
2
1

Output for Sample Input 2
3

Explanation of Output for Sample Input 2
Tasks 3, 4, and 5 can be completed in 6 minutes. It is not possible to complete more than 3 tasks
in 6 minutes.
"""

# Inputs
t = int(input()) # total available minutes
c_list = [] # each int represnets a chore and its length
for i in range(int(input())): # input is C
    c_list.append(int(input()))
c_list.sort()

# Enumerate
total = 0
output_n = 0
for chore in c_list: 
    if (total + chore < t):
        total += chore
        output_n += 1
    elif(total + chore == t):
        total += chore
        output_n += 1
        break
    else:
        break

# Final output
print(output_n)