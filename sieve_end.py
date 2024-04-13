def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)

    return primes

n = int(input("Podaj granicę:\n"))
primes = sieve_of_eratosthenes(n)
print("Liczby pierwsze do", n, "to:", primes)

import psutil
current_process = psutil.Process()
total_memory = psutil.virtual_memory().total
print("Całkowita dostępna pamięć RAM:", total_memory, "bytes")
memory_usage = current_process.memory_info().rss
print("Użycie pamięci przez bieżący proces:", memory_usage/1048576, "megabytes")
