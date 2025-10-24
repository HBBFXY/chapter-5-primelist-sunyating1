def primelist(n):
    is_prime = [True] * n
    if n > 0:
        is_prime[0] = False
    if n > 1:
        is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes
n = int(input())
result = primelist(n)
print(' '.join(map(str, result)))

