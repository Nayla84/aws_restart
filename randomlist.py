#Generate a random list of n from STDIN from sample: start, end from arguments
#start --> starting value
#end --> finish value

import random as ran
import sys 

start = int(sys.argv[1])
end = int(sys.argv[2])
n = int(input("Size = "))

numbers = ran.sample(range(start,end),n) #get n random values from the range

print(numbers)