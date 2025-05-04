#make a zero division error handler with built in exceptions.
def divide_numbers(a,b):
    try:
        result=a/b
        print("result:",result)
    except ZeroDivisionError:
        print("error:cannot divide by zero")
num1=float(input("enter num 1:"))
num2=float(input("enter num 2:"))
divide_numbers(num1,num2)
