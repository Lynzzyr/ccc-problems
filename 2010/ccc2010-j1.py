"""
CCC 2010 Problem J1

Problem Description

Natalie is learning to count on her fingers. When her Daddy tells her a number n (1 ≤ n ≤ 10),
she asks “What is n, Daddy?”, by which she means “How many fingers should I hold up on each
hand so that the total is n?”

To make matters simple, her Daddy gives her the correct finger representation according to the
following rules:

• the number may be represented on one or two hands;
• if the number is represented on two hands, the larger number is given first.

For example, if Natalie asks “What is 4, Daddy?”, her Dad may reply:

• 4 is 4.
• 4 is 3 and 1.
• 4 is 2 and 2.

Your job is to make sure that Natalie's Daddy gives the correct number of answers.

Input Specification
The input will be a single integer in the range 1..10.

Output Specification
The output is the number of ways of producing that number on two hands, subject to the rules
outlined above.

Sample Input
4

Output for Sample Input
3
"""

# Imports
import math

# Inputs
n = int(input())

# Parsing
if (n > 5):
    print(math.ceil((10 - n) / 2 + 0.5))
elif (n <= 5):
    print(math.ceil(n / 2 + 0.5))