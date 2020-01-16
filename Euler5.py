# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# must be divisible by the most number for prime factors that appear in any one of the numbers being divided by
# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 2 * 2
# 5 = 5
# 6 = 2 * 3
# 7 = 7
# 8 = 2 * 2 * 2
# 9 = 3 * 3
# 10 = 2 * 5
# 11 = 11
# 12 = 3 * 2 * 2
# 13 = 13
# 14 = 2 * 7
# 15 = 3 * 5
# 16 = 2 * 2 * 2 * 2
# 17 = 17
# 18 = 2 * 3 * 3
# 19 = 19
# 20 = 2 * 2 * 5


def find_roots(num):
    roots = []; product = 1; x = 2; number = num; y = number
    while product != number:
        while (y % x == 0):
            roots.append(x)
            y /= x
            product *= roots[-1]
        x += 1
    return roots

all_factors = []

for x in range(2, 20):
    all_factors.append(find_roots(x))

print(all_factors)