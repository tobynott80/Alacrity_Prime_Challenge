import prime
import argparse


parser = argparse.ArgumentParser(
    description="isPrime - a CLI to determine whether a integer (or array of integers) is prime"
)

parser.add_argument("--int", help="Check if an integer is prime")
parser.add_argument("--array", help="Check if an array is prime")


args = parser.parse_args()

if args.int:
    print(prime.isPrime(int(args.int)))

if args.array:
    array = args.array.split(",")
    formattedArray = []
    for i in array:
        formattedArray.append(int(i))
    print(prime.isArrPrime(formattedArray))
