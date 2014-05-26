# Problem 1: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Practice
nums = range(1,11)
mult35 = []
i = 0
total = 0

for num in nums[:-1]:

	if num%3 == 0:
		mult35.append(num)
	elif num%5 == 0:
		mult35.append(num)
for item in mult35:
	total = total + item
print(total)

# Problem #1
# Used while statement to set parameter for problem instead of writing list manually.
# Kept 'Practice' to demonstrate progress and alternative, albeit less efficient paths to the same solution.
mult35 = []
num = 1
total = 0

while num < 1000:
	if num%3 == 0:
		total = total + num
	elif num%5 == 0:
		total = total + num
	num = num + 1
print(total)