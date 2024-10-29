import sys
filename = sys.argv[1]
lines = open(filename).readlines()
print(lines)
numbers = [int(line) for line in lines]
print(numbers)
print(sum(numbers))
