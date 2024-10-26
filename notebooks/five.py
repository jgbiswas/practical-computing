import sys
filename = sysargv[1]
print(open(filename).readlines()[0:5])
