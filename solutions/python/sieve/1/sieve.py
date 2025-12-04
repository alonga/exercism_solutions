def primes(limit):
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, limit + 1, i):
                sieve[multiple] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]

