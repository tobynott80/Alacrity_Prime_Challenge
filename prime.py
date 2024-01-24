# Function to determine if a number (n) is prime
def isPrime(n):
    for i in range(2, (int(n / 2) + 1)):
        for j in range(2, (int(n / 2) + 1)):
            if (i * j) == n:
                ifPrime = False
                print(
                    "{i} and {j} are factors of {n}, therefore {n} is not prime".format(
                        i=i, j=j, n=n
                    )
                )
                return False
    return True


if __name__ == "__main__":
    print(isPrime(2))  # Expect: True
    print(isPrime(3))  # Expect: True
    print(isPrime(5))  # Expect: True
    print(isPrime(6))  # Expect: False
    print(isPrime(79))  # Expect: True
    print(isPrime(100))  # Expect: False
    print(isPrime(200))  # Expect: False
    print(isPrime(50))  # Expect: False
    print(isPrime(2000000))  # Expect: False
