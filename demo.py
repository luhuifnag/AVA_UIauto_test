alist = [] 

def a():
    global alist
    alist = [] 
    alist.append("10")

def b():
    print(alist)
a()
b()