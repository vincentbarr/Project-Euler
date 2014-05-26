# Problem #6: Sum square difference
# The sum of the squares of the first ten natural numbers is: 1^2 + 2^2 +... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

# Function 1 takes a range and finds the sum of the squares
# Function 2 takes a range and finds the square of the sum
import math

powerFixedSquare = 2;

def sumSquares(a,b):
  dataSet = range(a,b)
  sumSquaresResult = 0
  for n in dataSet:
    startingSum = math.pow(n,powerFixedSquare)
    sumSquaresResult = startingSum + sumSquaresResult
  return sumSquaresResult

def squareSums(a,b):
  dataSet = range(a,b)
  resultUnsquared = 0
  for n in dataSet:
    resultUnsquared = resultUnsquared + n
  squareSumsResult = math.pow(resultUnsquared, powerFixedSquare)
  return squareSumsResult

# Test: Returns 2640
# print(squareSums(1,11) - sumSquares(1,11))

print(squareSums(1,101) - sumSquares(1,101))
