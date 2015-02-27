#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove
#digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
#right to left: 3797, 379, 37, and 3.
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def prime(n):
    if (n % 2 == 0 and n > 2) or n < 2: 
        return False
    for i in range(3, int(n**.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def truncateLeft(n):
    while len(str(n)) > 1:
        n = int(str(n)[1:])
        if not prime(n):
            return False
    return True

def truncateRight(n):
    while len(str(n)) > 1:
        n = int(str(n)[:-1])
        if not prime(n):
            return False
    return True

l = []
n = 11
while len(l) < 11:
    if prime(n) and truncateLeft(n) and truncateRight(n):
        l.append(n)
    n += 2
print(l, sum(l))
