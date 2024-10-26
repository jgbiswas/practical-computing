import sys
filename = sys.argv[1]
print(open(filename).read().split("\n")[:5])
