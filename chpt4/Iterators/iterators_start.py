# define a list of days in English and French

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
daysdict = {"Sun": "Dim", "Mon": "Lun", "Tue":"Mar", "Wed":"Mer"
 ,"Thu":"Jeu", "Fri":"ven", "Sat":"Sam"}

 # TODO: iterator over a list
# print(days)
# print("using iter:")
# i = iter(days)
# print(next(i))
# print(next(i))
# print(next(i))


# TODO: iterator over a dictionary
print("dictionary iteration")
for key in daysdict:
    print(key, ":", daysdict[key])

print("\n ---------\n")

for k,v in daysdict.items():
    print(k, ":", v)

# TODO: use the enumerator fucntion
# print("using enumerate:")
# for i , m in enumerate(days, start=1):
#     print(i,m)

# TODO: using the zip function
# print("using zip:")
# for m in zip(days, daysFr):
#     print(m)
    


# TODO: combine enumate and zip
# print("usin enumarator with zip:")
# for i,m in enumerate(zip(days, daysFr), start=1):
#      print(f"Day {i}, {m[0]} is {m[1]} in French")