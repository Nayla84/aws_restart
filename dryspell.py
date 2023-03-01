#Read rain from STDIN until -1
#Determine the longest dry spell
#[dry spell is the longest dry days until it rains again]

import sys

#Objective ???? maximum dry days until rain > 0
maximum = -sys.maxsize

count = 0   #this counter is to count the dry days [rain = 0]

rain = int(input("Rain: ")) #reading the amount of rain

while rain !=-1:
    if rain == 0:
        count += 1
    else:
        maximum = max(maximum,count)
        count = 0
    rain = int(input("Rain: ")) 
maximum = max(maximum,count)    
print(f'Longest dry spell = {maximum}')
        
