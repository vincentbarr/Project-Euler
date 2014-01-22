# Problem 2: Even Fibonacci Numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

a = 1
b = 2
fibList = [1, 2]
fibListEven = []
lastChar = int(fibList[-1])
while int(fibList[-1]) + int(fibList[-2]) < 4000000:
	fibChar = int(fibList[-2]) + int(fibList[-1])
	fibList.append(fibChar)
fibListEven = [x for x in fibList if x%2 ==0]
print (sum(fibListEven))
