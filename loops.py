
print("while-loop output")
i = 0
while i < 10:
    print(i)
    i += 1 #Must update i
    
print("\nfor-loop output")
print("|   i | pow(i,2) |")
for i in range(0,10):
    print(f'| {i:3} | {pow(i,2):^8} |')