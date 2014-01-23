# Problem 3: Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Identify all prime factors of 600851475143

divisorList = range(2,60)
numberList = range(2,60)
primeList = []

for num in numberList:
	divisor = 2
	while divisor != num:
		if num%divisor == 0:
			break
		else:
			divisor = divisor +1
			if num%divisor == 0:
				break
			else:
			 if num - divisor == 1:
			 	primeList.append(num) 