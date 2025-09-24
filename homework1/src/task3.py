def check_number(n: int) -> str:
    # if its over 0 its positive else negative or 0
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def first_primes(limit=10):
    # finds prime numbers
    primes = []
    num = 2
    while len(primes) < limit:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1
    return primes

def sum_to_100():
    # returns the total of 1 to n of numbers
    total, n = 0, 1
    while n <= 100:
        total += n
        n += 1
    return total

