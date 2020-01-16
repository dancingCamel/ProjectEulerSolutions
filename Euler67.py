# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

import time

start = time.time()
pyramid = []
with open('euler67.txt', 'r') as file:

    for line in file:
        pyramid.append(line.split( ))

    x = 1


    while x < len(pyramid):
        y = 0
        while y < len(pyramid[x]):

            try:
                left = int(pyramid[x-1][y-1]) + int(pyramid[x][y])
            except:
                left = 0

            try:
                right = int(pyramid[x-1][y]) + int(pyramid[x][y])
            except:
                right = 0
            pyramid[x][y] = max(left, right)
            y+=1
        x+=1


print(max(pyramid[len(pyramid)-1]))
print(time.time()-start)