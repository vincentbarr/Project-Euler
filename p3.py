# Problem 3: Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Identify all prime factors of 600851475143

n = 600851475143
i = 2
while i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print (n)

# Helpful prime factorization concept: http://www.purplemath.com/modules/factnumb.htm