"""
CCC 2020 J2

Problem Description
People who study epidemiology use models to analyze the spread of disease. In this problem, we
use a simple model.

When a person has a disease, they infect exactly R other people but only on the very next day. No
person is infected more than once. We want to determine when a total of more than P people have
had the disease.

(This problem was designed before the current coronavirus outbreak, and we acknowledge the
distress currently being experienced by many people worldwide because of this and other diseases.
We hope that including this problem at this time highlights the important roles that computer
science and mathematics play in solving real-world problems.)

Input Specification
There are three lines of input. Each line contains one positive integer. The first line contains the
value of P . The second line contains N , the number of people who have the disease on Day 0. The
third line contains the value of R. Assume that P ≤ 107 and N ≤ P and R ≤ 10.

Output Specification
Output the number of the first day on which the total number of people who have had the disease
is greater than P.

Sample Input 1
750
1
5

Output for Sample Input 1
4

Explanation of Output for Sample Input 1
The 1 person on Day 0 with the disease infects 5 people on Day 1. On Day 2, exactly 25 people
are infected. On Day 3, exactly 125 people are infected. A total of 1 + 5 + 25 + 125 + 625 = 781
people have had the disease by the end of Day 4 and 781 > 750.

Sample Input 2
10
2
1

Output for Sample Input 2
5

Explanation of Output for Sample Input 2
There are 2 people on Day 0 with the disease. On each other day, exactly 2 people are infected. By
the end of Day 4, a total of exactly 10 people have had the disease and by the end of Day 5, more
than 10 people have had the disease.
"""

# Inputs
p = int(input())
n = int(input())
r = int(input())

# Iterations
counter = 0
infected = n
while infected <= p:
    infected += n * r
    n *= r
    counter += 1

# Final output
print(counter)