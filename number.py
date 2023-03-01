x = input("Enter a number: ")

#Nested if-statement
if x.isnumeric():
    if int(x) > 0:
        print("x is positive")
    elif int(x) < 0:
        print("x is negative")
    else:
        print("x is zero")
else:
    print("x is not a number")