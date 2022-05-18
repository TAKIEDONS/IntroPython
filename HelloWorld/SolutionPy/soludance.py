# Example HelloWorld file for the python for the C# Developer LinkedIn Learning course
print("Music Entertainment")

print("Enter a number to start the bally, enter 'quit' to stop")

strname = input("Enter your name babe!!!")

select = True
total = 0

while(select):
    try:
        # use the input method to read the command line
        strsong = input("enter name songs: ")
        if strsong == "":
            select = False
        else:
            # the int function tries to convert the input to an integer
            # val = int(str)
            total += int(strsong)
            print(strname)
            print(total)

    except ValueError:
        # if int() throws an error then we ignore it and keep gpoing

      pass