# Example HelloWorld file for the python for the C# Developer LinkedIn Learning course

from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from operator import truediv

print("RunningTally(tm)")

print("Enter a number to start the bally, enter 'quit' to stop")
run = True
total = 0

while(run):
    try:
        # use the input method to read the command line
        str = input()
        if str == "quit":
            run = False
        else:
            # the int function tries to convert the input to an integer
            val = int(str)
            total +=val
            print(total)

    except ValueError:
        # if int() throws an error then we ignore it and keep gpoing

      pass