# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

longest_chain = 0
from_number = 1

def even(num):
    return num/2

def odd(num):
    return (3*num+1)

for x in range(2, 1000000):
    temp_number = x
    temp_chain_length = 0
    while temp_number != 1:
        if temp_number % 2 == 0:
            temp_number = even(temp_number)
            temp_chain_length += 1
        else:
            temp_number = odd(temp_number)
            temp_chain_length += 1
    if temp_chain_length > longest_chain:
        longest_chain = temp_chain_length
        from_number = x

print(longest_chain)
print(from_number)


