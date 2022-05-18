fruitlist = ['orange','banana','melon'] # declare an empty list
listwithdata = ['a', 1, True, "Bob"] # declare a list with contetnt

# TODO: append data to list

fruitlist.append("apple")
fruitlist.append(['orange','banana','melon'])

# TODO: insert data
fruitlist.insert(2, "grape")
fruitlist.insert(3, "mango")
print(fruitlist)

# TODO: search for a list item
print("pear" in fruitlist)
index = fruitlist.index('melon')
print(index)


# TODO: modify an item in-place
fruitlist[3]="pawpaw"
print(fruitlist)

# TODO: remove an item
fruitlist.remove("grape")
print(fruitlist)

# TODO: empty the list
fruitlist.clear()
print(fruitlist)

# TODO: lists can be created using list() gloabl fucntion
chars = list("abcdefg")
print(chars)

nums = list(range(50,100,5))
print(nums)