# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

from functools import reduce
import time

start_time = time.time()

def triangle_number_iterator():
    index = 1
    triangle_number = 1
    while True:
        index += 1
        triangle_number += index
        yield triangle_number

# found this function online
def find_factors(num):
    return set(reduce(list.__add__, ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0))) # gets pair of factors then only checks smaller one, up to sqrt number

for number in triangle_number_iterator():
    if (len(find_factors(number))) > 500:
        print(number)
        break

print(time.time()-start_time)