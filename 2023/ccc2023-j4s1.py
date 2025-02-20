"""
CCC 2023 J4/S1

Problem Description

Bocchi the Builder just finished constructing her latest project: a laneway consisting of two
rows of white equilateral triangular tiles. However, at the last moment, disaster struck! She
accidentally spilled black paint on some of the tiles. Now, some of the tiles are wet and the
other tiles are dry. Bocchi must place warning tape around the perimeters of all wet areas.
Can you help her determine how many metres of tape she needs?

The first triangular tile will point upwards. Each pair of adjacent tiles (that is, tiles that
share a common side) will point in opposite directions. Each tile has a side length of 1 metre.

Input Specification
The first line of input will consist of one positive integer C, representing the number of
columns.

The next two lines will each consist of C integers separated by spaces. Each integer represents
the colour of a tile along the laneway, with 1 indicating that the tile is black (wet) and 0
indicating that the tile is white (dry).

Output Specification
Output a single integer representing the length of tape Bocchi needs, in metres.

Sample Input 1
5
1 0 1 0 1
0 0 0 0 0

Output for Sample Input 1
9

Explanation of Output for Sample Input 1
The tiles are painted as follows, creating three wet areas. Bocchi will need 9 metres of
warning tape as shown in yellow.

Sample Input 2
7
0 0 1 1 0 1 0
0 0 1 0 1 0 0

Output for Sample Input 2
11

Explanation of Output for Sample Input 2
The tiles are painted as follows, creating three wet areas. Bocchi will need 5 metres of
warning tape to surround one area and 3 metres of warning tape to surround each of the
other two areas as shown in yellow.
"""

