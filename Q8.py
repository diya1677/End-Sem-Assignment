#make module not found error handler with built in exception
try:
    import non_existent_module
except ModuleNotFoundError:
    print("ERROR:MODULE NOT FOUND")
