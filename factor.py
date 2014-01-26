# Function to find all factors of an number

# Importing functtols because the reduce function depends on it
import functools

# Defining factors function
def factors(n):

# Set is getting rid of duplicates, such as factors of 4 [2, 2]
# reduce(list.__add__,...) takes the lists of [fac1, fac2] and adds them into one long list
# [i, n/i] for i in range(1, int(sqrt(n)) +1) if n % i == 0 returns a pair of factors
# if the remainder when I divide n by the smaller one is zero.
# (It doesn't need to check the large one, too, it just gets that dividing n by the smaller one)

   return set(functools.reduce(list.__add__,
      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# Further explanation of this code as it was borrowed as a model for 'efficient' code: http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python