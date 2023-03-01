import sys

length = len(sys.argv) #list of arguments given to the script

if length == 1:
    print(sys.argv[0]+" has no argument")
elif length == 2:
    print(sys.argv[0]+" has one argument: "+sys.argv[1])
else:
    print("Argument list: "+str(sys.argv))