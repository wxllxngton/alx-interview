#!/usr/bin/python3
"""
Script simulates a game between 'Maria' and 'Ben'.
"""


def is_prime(n):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    """
    Generate a list of primes up to n using the Sieve of Eratosthenes.

    Parameters:
    n (int): The upper limit to generate primes.

    Returns:
    list: A list of prime numbers up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


def play_game(n):
    """
    Simulate a single game of removing primes and their multiples.

    Parameters:
    n (int): The upper limit of the consecutive integers.

    Returns:
    str: 'Maria' if Maria wins, 'Ben' if Ben wins.
    """
    primes = generate_primes(n)
    is_maria_turn = True
    current_numbers = set(range(1, n + 1))

    while True:
        available_primes = [p for p in primes if p in current_numbers]
        if not available_primes:
            return 'Ben' if is_maria_turn else 'Maria'

        choice = available_primes[0]
        multiples_to_remove = {choice * i for i in range(1, (n // choice) + 1)}
        current_numbers -= multiples_to_remove
        is_maria_turn = not is_maria_turn


def isWinner(x, nums):
    """
    Determine the winner of the most rounds between Maria and Ben.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing
    the upper limit for each round.

    Returns:
    str: The name of the player that won the most rounds or None if it's a tie.
    """
    won_rounds_maria = 0
    won_rounds_ben = 0

    for num in nums[:x]:
        winner = play_game(num)
        if winner == 'Maria':
            won_rounds_maria += 1
        else:
            won_rounds_ben += 1

    if won_rounds_maria > won_rounds_ben:
        return 'Maria'
    elif won_rounds_ben > won_rounds_maria:
        return 'Ben'
    else:
        return None
