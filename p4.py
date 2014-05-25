# Problem 4: Largest Palindrome Product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Smallest 3 digit number: 100
# Largest 3 digit number: 999
# Answer is 5 - 6 digits
# Since the number cannot start with 0, it cannot end with 0
# Therefore, it is not divisible by 10.
# So, the three digit numbers are [1-9][0-9][1-9], 810 possibilities.

def is_palindrome(i):
	return str(i) == str(i)[::-1]

max_palindrome = 0

# Starting from 101 because it can't end in 0
for i in range(1, 999):
# first pass: for range, (101, 105): i is 101
# second pass: i is 102
#	Test: print('i is', i)
	for j in range(i, 999):
# first pass: for range (101, 105) j is i + 1, so 102
# j is i + 2, so 103
# j is i +3, so 104 (runs up to last integer of range -1 (so, 104))
# second page: j is 103, 104
# Test: print('J is', j)
		p = i * j
		if is_palindrome(p) and p > max_palindrome:
			max_palindrome = p

print (max_palindrome)
