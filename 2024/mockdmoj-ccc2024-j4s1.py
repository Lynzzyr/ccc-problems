"""
DMOJ Mock CCC 2024 Problem J4/S1

Problem Description

You are given a row of slots numbered from 1 to N . Each slot can either be vacant (0) or contain a magnetic marble (1). The magnetic forces in these marbles
prompt adjacent ones to merge into a single marble, settling in the slot of the rightmost merging marbles. Marbles merge immediately when adjacent, including in the
starting configuration. Your task is to place exactly K marbles such that the resulting number of marbles is the minimum possible.

Input Specification
The input will consist of two lines. The first line will contain two integers N and K , representing the number of slots and number of marbles that you can add
respectively.

The second line will contain a string of 0 and 1 of length N .

Output Specification
The output will consist of a single integer indicating the minimum possible number of marbles in the slots after all marbles have been placed.

Sample Input 1
6 1
010111

Sample Output 1
2

Explanation for Sample 1
In the given example, the row of slots can be represented as 010111 at the beginning. We can perform a merge immediately, and the configuration becomes
010001. We can place one marble at the first slot and result in the configuration 110001. Then, another merge can be performed, and our final configuration
becomes 010001 which has the minimum possible number of marbles after all marbles are placed and merged.

Sample Input 2
30 9
100010000000001001001000001001

Sample Output 2
3
"""

# Functions
def merge_to_right(merge_input: str):
    merge_output = ""
    i = -1

    while True:
        if i == -len(merge_input):
            merge_output = merge_input[i] + merge_output
            break

        if not (merge_input[i] == "1" and merge_input[i - 1] == "1"):
            merge_output = merge_input[i] + merge_output
            i -= 1
            continue

        adj_nums = 1
        i -= 1

        while True:
            if merge_input[i - 1] == "1":
                adj_nums += 1
                i -= 1

            else:
                break

        i -= 1
        
        merge_output = "0" * adj_nums + "1" + merge_output
    
    return merge_output

def count_zero_groups(count_input: str):
    list_from_in = sorted([curr for curr in count_input.split("1") if curr != ""])

    count_dict = {}
    longest_zeros = 0

    for zeros in list_from_in:
        if len(zeros) > longest_zeros:
            count_dict.update({len(zeros): 1})
            longest_zeros = len(zeros)
            continue

        count_dict.update({longest_zeros: count_dict.get(longest_zeros) + 1})
    
    return count_dict

# Inputs
N = int(input())
K = int(input())
marbles = input()

# Main logic
if 