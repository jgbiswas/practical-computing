import sys
import random
import string
mylist = string.ascii_letters + string.digits 
print([random.choice(mylist) for i in range(int(sys.argv[1]))])

    
