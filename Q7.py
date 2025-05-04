#make a file not found error handler with built in exception
filename="data.txt"
try:
    file=open(filename,"r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("error:file not found")
    with open (filename,'w')as file:
        file.write("this is a new file")

