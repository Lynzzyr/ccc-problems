"""
CCC 2012 J4

Problem Description
Sheldon and Leonard are physicists who are fixated on the BIG BANG theory. In order to exchange
secret insights they have devised a code that encodes UPPERCASE words by shifting their letters
forward.

Shifting a letter by S positions means to go forward S letters in the alphabet. For example, shifting
B by S = 3 positions gives E. However, sometimes this makes us go past Z, the last letter of
the alphabet. Whenever this happens we wrap around, treating A as the letter that follows Z. For
example, shifting Z by S = 2 positions gives B.

Sheldon and Leonard's code depends on a parameter K and also varies depending on the position
of each letter in the word. For the letter at position P , they use the shift value of S = 3P + K.

For example, here is how ZOOM is encoded when K = 3. The first letter Z has a shift value
of S = 3 x 1 + 3 = 6; it wraps around and becomes the letter F. The second letter, O, has
S = 3 x 2 + 3 = 9 and becomes X. The last two letters become A and B. So Sheldon sends
Leonard the secret message: FXAB

Write a program for Leonard that will decode messages sent by Sheldon.

Input Specification
The input will be two lines. The first line will contain the positive integer K (K < 10), which
is used to compute the shift value. The second line of input will be the word, which will be a
sequence of uppercase characters of length at most 20.

Output Specification
The output will be the decoded word of uppercase letters.

Sample Input 1
3
FXAB

Output for Sample Input 1
ZOOM

Sample Input 2
5
JTUSUKG

Output for Sample Input 2
BIGBANG
"""

# Imports
import math

# Input
k = int(input())
input_sequence = input()
output = ""

# Iterate through input
for i in range(len(input_sequence)):
    unicode_point = ord(input_sequence[i])
    s = 3 * (i + 1) + k # using i as position requires i + 1 because i starts counting at 0
    wraps = math.floor(s / 26)
    if (unicode_point - s < 65) : wraps += 1
    if (unicode_point - s < 65) and (math.floor(s / 26)) : wraps -= 1
    
    unicode_point += wraps * 26 - s

    output += chr(unicode_point)

# Final output
print(output)