# functions are defined using the def keyword, then
# the : character and whitespace define the function body

def myfunc():
    print("This is a line in my function")
    return 42

def myvoidfunc(a, b):
    print("This function returns nothing")
    print(a+b)

def  variableargs(a,b, *args):
        print(a+b)
        for arg in args:
            print(arg)

retval = myfunc()
print(retval)

retval = myvoidfunc(5,10)
print(retval)

variableargs(1,2, "Takalani", "Humbu",8, 67)