#make value error handler with built in exception
x=9
y=0
print(x)
try:
    a=x/y
except ZeroDivisionError:
    print("error:cannot divide by zero")
except ValueError :
    print('error in code')

print(x)
print(y)
