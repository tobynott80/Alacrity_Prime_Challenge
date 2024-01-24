# Function to determine if a number (n) is prime by finding one factors (modulus operator)
def isPrime(n):
    if n <= 1:  # 1 is not prime, zero is not prime, negative numbers are not prime
        return False
    # Loop through each possible factor (stop halfway through, because if a factor exists, we would have found it by then)
    for i in range(2, (int(n / 2) + 1)):
        # Modulo check to see if i is a factor of n (i.e when n is divided by i, is the remainder 0?)
        if n % i == 0:
            print("{} is a factor of {}, not prime".format(i, n))
            return False
    return "Prime!"


# Returns an array of the prime numbers in a given array of integers
def isArrPrime(arr):
    primes = []
    for n in arr:  # Loop through given array
        if isPrime(n):
            primes.append(n)  # append to primes array if is prime
    return primes


if __name__ == "__main__":
    print(isPrime(2))  # Expect: 'Prime!'
    print(isPrime(3))  # Expect: 'Prime!'
    print(isPrime(5))  # Expect: 'Prime!'
    print(isPrime(9))  # Expect: False
    print(isPrime(79))  # Expect: 'Prime!'
    print(isPrime(100))  # Expect: False
    print(isPrime(200))  # Expect: False
    print(isPrime(50))  # Expect: False
    print(isPrime(2000000))  # Expect: False

    print(isArrPrime(range(2, 100)))

    print(isPrime(0))
    print(isPrime(1))
    print(isPrime(-17))
