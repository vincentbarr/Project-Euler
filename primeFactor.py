# Function to find all prime factors of a number

def primes(n):
    primeList = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primeList.append(d)
# Divides left operand by right operand and assigns the result to the left operand, n
            n /= d
        d += 1
    if n > 1:
       primeList.append(n)
    return primeList