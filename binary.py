#Read a value between 0 and 255 from STDIN
#Convert this value to binary representation

n = input("N = ")
while not(n.isnumeric()):
    n = input("Try again N = ")

N = int(n)
        
list1 = []
zeros = [0,0,0,0,0,0,0,0]

while N > 0:
    list1.append(N%2)
    N = int(N/2);
reverse = list(reversed(list1))   
binary = zeros[len(reverse):len(zeros)]+reverse
print(binary)