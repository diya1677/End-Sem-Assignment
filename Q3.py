# MAKE a key error handler with built in exceptions
my_dict={"name":"siya","age":20,"city":"ddun"}
try:
    print(my_dict["gender"])
except KeyError:
    print("error:key not found")
