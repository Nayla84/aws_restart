#Read a sentence from STDIN
#print the characters of the string on the same line separated by comma
#Count the number of spaces in this sentence

string = input("Sentence: ")

for c in string:
    print(c, end=", ")
print()   

i=0 
count = 0   
while i < len(string):
    if string[i] == ' ':
        count +=1
    i +=1
print("Spaces count = "+str(count))

