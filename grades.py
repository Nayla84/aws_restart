#Read the name of the student from STDIN (user-input)
#Give the mark of the student as argument to the script
#Determine the grade of the student based on the mark
import sys 

name = input("Name: ")
mark = int(sys.argv[1])

#Cascaded if-statement
if mark >= 85:
    grade = "HD"
elif mark >= 75:
    grade = "D"
elif mark >= 65:
    grade = "C"
elif mark >= 50:
    grade = "P"
else:
    grade = "Z"
    
print("welcome {}, your mark is {} and grade is {}".format(name,mark,grade))
print(f'Welcome {name}, your mark is {mark} and grade is {grade}')   

