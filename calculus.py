#Read integers until -1 from STDIN
#Determine the sum of all values
#Determine the min and max of all values
#Determine the average at 3 decimal points
import sys
n = int(input("N = "))

total = 0
minimum = sys.maxsize #2**63  -1  (biggest value in the system)
maximum = -sys.maxsize
count = 0
while n != -1:
    total += n
    if minimum > n:
        minimum = n
    if maximum < n:
        maximum = n
    count += 1
    n = int(input("N = "))
    
print(f'Total = {total}')
print(f'Min = {minimum}')
print(f'Max = {maximum}')
print(f'Average = {total/count:.3f}')