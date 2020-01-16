# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million

import math

def check_prime(num):
    is_prime = True
    for x in range(2, int(math.ceil(math.sqrt(num)))+1):
        if num%x == 0:
            is_prime = False
            break
    return is_prime

sum = 2

for i in range(3, 2000000, 2):
    if check_prime(i):
        sum += i

print(sum)