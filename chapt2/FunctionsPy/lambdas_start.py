
data = [10, 6, 23, 15, 18, 59, 62, 103, 29, 35]

# regular sort
print("Sorted:")

result = sorted(data)
print(result)

# TODO: sort using a lamda
print("Sort by first digit")
result = sorted(data, key=lambda x: str(x)[0])