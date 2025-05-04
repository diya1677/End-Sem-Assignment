#make a index error handler with built in exception
def get_item(l,index):
    try:
        return l[index]
    except IndexError:
        print("error:index not found")
        return None
flower=['rose','daisy','marigold','blossom']
print(get_item(flower,3))
print(get_item(flower,6))
    
