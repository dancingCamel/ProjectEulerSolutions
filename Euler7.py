# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
import math, time

start = time.time()

def check_prime(num):
    is_prime = True
    for x in range(2, int(math.ceil(math.sqrt(num)))+1):
        if num%x == 0:
            is_prime = False
            break
    return is_prime


def find_prime_at_index(num):
    index = 1
    prime = 2
    temp = 3
    while True:
        if index == num:
            break
        if check_prime(temp):
            prime = temp
            index += 1
            temp += 2
        else:
            temp += 2
    return "The prime at index {} is {}".format(index, prime)

print(find_prime_at_index(10001))
print(time.time() - start)