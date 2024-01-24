# Function to determine if a number (n) is prime by finding two factors
def isPrime(n):
    # Loop through each possible factor upto n/2 and then check for possible factors with a nested loop
    for i in range(2, (int(n / 2) + 1)):
        for j in range(2, (int(n / 2) + 1)):
            # if two factors are found:
            if (i * j) == n:
                print(
                    "{i} and {j} are factors of {n}, therefore {n} is not prime".format(
                        i=i, j=j, n=n
                    )
                )
                return False
    return "Prime!"


# Function to determine if a number (n) is prime by finding one factors (modulus operator)
def isPrimeV2(n):
    # Loop through each possible factor (stop halfway through, because if a factor exists, we would have found it by then)
    for i in range(2, (int(n / 2) + 1)):
        if (
            n % i == 0
        ):  # Modulo check to see if i is a factor of n (i.e when n is divided by i, is the remainder 0?)
            print("{} is a factor of {}, not prime".format(i, n))
            return False
    return "Prime!"


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

    print(isPrimeV2(2))  # Expect: 'Prime!'
    print(isPrimeV2(3))  # Expect: 'Prime!'
    print(isPrimeV2(5))  # Expect: 'Prime!'
    print(isPrimeV2(6))  # Expect: False
    print(isPrimeV2(79))  # Expect: 'Prime!'
    print(isPrimeV2(100))  # Expect: False
    print(isPrimeV2(200))  # Expect: False
    print(isPrimeV2(50))  # Expect: False
    print(isPrimeV2(2000000))  # Expect: False
