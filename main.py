import prime
import argparse


parser = argparse.ArgumentParser(
    description="isPrime - a CLI to determine whether a integer (or array of integers) is prime"
)

parser.add_argument("--int", help="Check if an integer is prime")
parser.add_argument("--array", help="Check if an array is prime")
parser.add_argument(
    "--range", help="Format min,max. Check if a range of integers is prime"
)


args = parser.parse_args()

if args.int:
    print(prime.isPrime(int(args.int)))

if args.array:
    array = args.array.split(",")
    formattedArray = []
    for i in array:
        formattedArray.append(int(i))
    print(prime.isArrPrime(formattedArray))

if args.range:
    minmax = args.range.split(",")
    formattedRange = range(int(minmax[0]), int(minmax[1]))
    print(prime.isArrPrime(formattedRange))
