# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
import time

start = time.time()

def check_palindrome(num):
    string = str(num)
    if string == string[::-1]:
        return True

largest = 0
for num in range(999, 900, -1):
    for num2 in range (999, 900, -1):
        if check_palindrome(num*num2) and num*num2>largest:
            largest = num*num2

print(largest)
print(time.time()-start)