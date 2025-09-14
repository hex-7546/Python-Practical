def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num (int): Number to check.
        
    Returns:
        bool: True if prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primes_till_n(n):
    """
    Generate all prime numbers till n (inclusive).
    
    Args:
        n (int): Upper limit
    
    Returns:
        list: List of primes up to n
    """
    primes = []
    for number in range(2, n + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def first_n_primes(n):
    """
    Generate the first n prime numbers.
    
    Args:
        n (int): Number of primes to generate
    
    Returns:
        list: First n prime numbers
    """
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Main program
try:
    n = int(input("Enter a positive integer n: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        # a. Check if n is prime
        if is_prime(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")

        # b. Generate all prime numbers till n
        print(f"Prime numbers till {n}: {primes_till_n(n)}")

        # c. Generate first n prime numbers
        print(f"First {n} prime numbers: {first_n_primes(n)}")

except ValueError:
    print("Invalid input. Please enter a valid positive integer.")