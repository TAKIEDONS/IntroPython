# Exceptions in python are similar to those in C#
# There's a try-except-finally machanism

try:
    a=30
    b=5
    d = 7
    # c= None
    # # if (a > 20):
    # #     raise ValueError("Can't go higher than 20!")

    x = a + b * d
    print("Result is", x)
except ZeroDivisionError as e :
    print("Whoops! ", e)
except ValueError as e:
    print("uh oh", e)
except BaseException as e:
    print(e)
finally:
    print("this code always runs")


# https://docs.python.org/3/tutorial/errors.html#exceptions