#make a error handler with the use of multiple except for all type of errors
try:
    #simulate diffremt errorr by commenting one at a time
    #num=int(abc)
    #div=10/0
    #l1=[33,55,84,92,04]
    #print(l1[6])
    #dict={"a":22,"b":"flower","c":1223}
    #print(dict["e"])
    #x=55
    #x.isalpha
    #open("nots.txt","r")
    #import fake_module
    print("block parameterr")
except ValueError:
    print("ERROR VALUE NOT FOUND")
except ZeroDivisionError:
    print("ZERO ERROR")
except IndexError:
    print("INDEX NOT FOUND")
except KeyError:
    print("key is not there")
except AttributeError:
    print("WRONG ATTRIBUTE")
except FileNotFoundError:
    print("FILE NOT FOUND")
except ModuleNotFoundError:
    print("INVALID MODULE ")
    
    
    
    
