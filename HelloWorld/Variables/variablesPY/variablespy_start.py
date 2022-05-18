# TODO: variables can be declared without an explicit type
from string import printable


f=0
print(f)
b= True
print(b)
# TODO: re-declaring  the variable works
f = "abc"
print(f)

# TODO: ERROR: variable of different types cannot be combined

print("string type" + str(123))

# TODO: Global vs. local variables in functions

def somefunction():
    global f
    f= "def"
    print(f)

somefunction()
print(f)
# TODO: use the del operator to undeclare variable
del f
print(f)