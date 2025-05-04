#make attribute error handler with built in exception
text=123
try:
    result=text.isupper()
except AttributeError:
    print("error ")
    
