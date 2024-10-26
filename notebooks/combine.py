import sys
lines = open(sys.argv[1]).readlines() + open(sys.argv[2]).readlines()
with open(sys.argv[3], "w") as f:
    for line in lines:
        f.write(line)
print(open(sys.argv[3]).read().strip())
