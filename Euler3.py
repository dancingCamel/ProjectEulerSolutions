# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
import math

def check_prime(num):
    is_prime = True
    for x in range(2, int(math.ceil(math.sqrt(num)))+1):
        if num%x == 0:
            is_prime = False
            break
    return is_prime


def find_factors(num):
    for x in range(2, int(math.ceil(num/2)+1)):
        if num%x == 0:
            yield x


def prime_factors(num):
    for i in find_factors(num):
        if check_prime(i):
            yield i

test_number = 600851475143
break_test = 1

for x in prime_factors(test_number):
    print(x)
    break_test *= x
    if break_test == test_number:
        break

