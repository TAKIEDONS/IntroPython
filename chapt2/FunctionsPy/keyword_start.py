# python provides a way to ruquire that some arguments can only be called
# by keyword. This is usually used when the argument is importment and you
# want the caller to explicitly use the argument name

def myFunction(arg1, arg2, *, suppressExceptions=False):
    print(arg1, arg2, suppressExceptions)

myFunction(1, 56, suppressExceptions=True)    