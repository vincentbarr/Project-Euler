# Problem 4: Largest Palindrome Product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Smallest 3 digit number: 100
# Largest 3 digit number: 999
# Answer is 5 - 6 digits
# Since the number cannot start with 0, it cannot end with 0
# Therefore, it is not divisible by 10. 
# So, the three digit numbers are [1-9][0-9][1-9], 810 possibilities.

n = 0
for i in range (1,10):
	for j in range (0,10):
		for k in range (1,10):
			sameNum = (i*100) + (j*10) +k
			resultSame = str(sameNum*sameNum)
			if resultSame == resultSame[::-1]:
				print (sameNum,sameNum)
			for l in range(1,10):
				for m in range (0,10):
					for n in range (1,10):
						diffNum = (l*100) + (m*10) + n
						resultDiff = str(sameNum*diffNum)
						if resultDiff == resultDiff[::-1]:
							print (resultDiff, diffNum, sameNum)