#!/usr/bin/python3

def eratosthenes(max_n):
    '''Seiv of Eratosthenes algorithm to find all primes up to max_n'''
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    primes = []
    for i in range(2, max_n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes, is_prime


def isWinner(x, nums):
    max_n = max(nums)
    primes, is_prime = eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        remaining = [True] * (n + 1)
        remaining[0] = remaining[1] = False

        maria_turn = True
        while True:
            move_made = False
            for p in primes:
                if p > n:
                    break
                if remaining[p]:
                    for multiple in range(p, n + 1, p):
                        remaining[multiple] = False
                    move_made = True
                    break

            if not move_made:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
