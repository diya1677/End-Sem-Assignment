my_list = []

def append1(x):
    my_list.append(x)
    print("List after append:", my_list)

def extend1(l):
    my_list.extend(l)
    print("List after extend:", my_list)

def pop():
    if my_list:
        my_list.pop()
    print("List after pop:", my_list)

def remove1(x):
    if x in my_list:
        my_list.remove(x)
    print("List after remove:", my_list)
