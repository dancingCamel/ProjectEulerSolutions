# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52. (2 = sqr)
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

limit = 1000

def check_triplet(x, y):
    z = math.sqrt(x**2 + y**2)
    if z.is_integer():
        return int(z)
    else:
        return False

for i in range(1, limit):
    for j in range(1, limit):
        if check_triplet(i, j) != False:
            if (i + j + check_triplet(i, j)) == 1000:
                print(i * j * check_triplet(i, j))

