# Exercise file for python for the C#

# Functions can then be called using named parameters
# once you use a named parameter, all following params must be 
# called by name as well

def namedparams(a, b, c):
    if c:
        print("'a' comes")
        print(a)
        print(b)
    else:
        print("'b' comes first")
        print(b)
        print(a)

namedparams(5, b="hello", c=True)

