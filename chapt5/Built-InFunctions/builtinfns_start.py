# Define some data to use in our functions
numbers = [10, 6, 23, 15, 18, 59, 7, 103, 29, 35]
names = ["Amy", "Adam", "Benjamin", "Elise", "Terry", "ziggy"]
somestr = "The quick brown fox jumped over the lazy dog"

# # TODO: Then len fucntion will return the length of any iterable
# print(len(numbers))
# print(len(somestr))

# # TODO: min and max calculate the smallest and largest values
# minnum = min(numbers)
# maxnum = max(numbers)
# print(minnum, maxnum)

# # TODO: min and max can also a key function to provide a comparable value
minnum = min(names, key=lambda x: len(x))
maxnum = max(names, key=lambda x: len(x))
print(minnum, maxnum)

# TODO: The sorted function will return a new sorted list an iterable 
# print(sorted(numbers))
# print(sorted(somestr))
# print(sorted(names, key=lambda x: len(x)))
# # TODO: any and all can used to perform a test a test on a set of data
# print(any(len(w)> 5 for w in names))
# print(all(x > 20 for x in numbers))
