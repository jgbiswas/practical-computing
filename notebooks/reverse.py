import sys
lines = open(sys.argv[1]).readlines()[::-1]
with open(sys.argv[1], "w") as f:
    for line in lines:
        f.write(line)
print(open(sys.argv[1]).read())            
