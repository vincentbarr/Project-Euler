
# Problem 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 2520 is divisible by 1-10, as well as 12,14,15,16,18, and 20. However, it is is not disibile by 11, 13, 17, or 19: the prime numbers.

factorList = [11, 13, 14, 16, 17, 18, 19, 20]

def find_LCM(targetNumber):
    for num in xrange(targetNumber, 100000000000000000, targetNumber):
        if all(num % n == 0 for n in factorList):
            print(num)
            return num

find_LCM(2520)