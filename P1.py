nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mult35 = []
i = 0
total = 0

for num in nums[:-1]:

	if num%3 == 0:
		mult35.append(num)
	if num%5 == 0:
		mult35.append(num)
for item in mult35:
	total = total + item
print(total)