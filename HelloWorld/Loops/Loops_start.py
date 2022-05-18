# python for the C# Developer by Joe Marini
# Example code file for loops

# (init value, test, increament) pattern isn't something you see in python

# TODO: ti interate over a count, you create a numerical iterator with range

# print("\n--------------")

# for i in range(10):
#     print(i, end=" ")


# print("\n--------------")

# for i in range(-5, 5, 2):
#     print(i, end=" ")

# TODO: iterating over a collection or string is the same as with C# for each
# but we use the same "for" keyword

# thestr = "Hello World!"
# for c in thestr:
#     print(c + ",", end=" ")

# print("\n--------------")

# # TODO: if you really need an index, you can use enumerate()
# for i, c in enumerate(thestr):
#     print(str(i) + ", "+ ", ", end="")

# print("\n--------------")

# TODO: Similarly, there's only a while loop in python and no do- while
# is just syntactic sugar for a loop that always executes at least once
# program for QR attendance on Discord 

from ast import While

print("QRSpace program on Discord")
print("\n--------------")

online = True
online_candidates= ["takalani", "beur", "james", "Molo"]
offline_condidates= ["james","Nathen","Yakshin"]

i = 0 
while (online):
     print("online candidates")
     print(online_candidates)
     i +=1

     if i==1:
          print("offline candidates")
          print(offline_condidates)
          online=False
       

 # TODO: Similarly, there's only a while loop in python and no do- while

Keepgoing = True
i = 0 

while (Keepgoing):
    print("num: ", i)
    i+=1

    if i ==10:
       Keepgoing=False
       print("thats all")





