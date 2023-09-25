"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True  

def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError("wrong input")
    list = []
    number = 2
    while len(list)<number_of_primes:
        if isPrime(number):
            list.append(number)
        number+=1
    return list
