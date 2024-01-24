# Alacrity_Prime_Challenge

## Using the CLI:

### For a single integer

`python .\main.py --int [integer]`

E.g for checking if 6 is prime:

```
$ python .\main.py --int 6
2 is a factor of 6, not prime
False
```

### For an array

`python .\main.py --array [array]`

> Note: array format should be integers separated by commas
> E,g for checking the array 1,6,10,7:

```
$ python .\main.py --array 1,6,10,7
2 is a factor of 6, not prime
2 is a factor of 10, not prime
[1, 7]
```

### For a range

`python .\main.py --range min,max`

For example, checking the range 1 to 100:

```
$ python .\main.py --range 1,100
2 is a factor of 4, not prime
2 is a factor of 6, not prime
2 is a factor of 8, not prime
...
2 is a factor of 96, not prime
2 is a factor of 98, not prime
3 is a factor of 99, not prime
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```
