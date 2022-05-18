# declare an empty dictionary
fileDesc ={}

# dictioanaries can also be declared with initial content
nums = {1: "one", 2 : "two", 3: "three"}

# TODO: add some items
fileDesc["pdf"] = "Portable Document Format"
fileDesc["txt"] = "Text file"
fileDesc["rtf"] = "Rich Text Format"
fileDesc["jpg"] = "JPEG Image"
fileDesc["png"] = "Portable Network Graphic Image"



# TODO: get the item count

print(f"Dictionary contains {len(fileDesc)} items")

# TODO: adding an existing key just replaces the item
fileDesc["png"] = "PNG File"
print(fileDesc["png"])

# TODO: check if a key exists
print("txt" in fileDesc.keys())

# TODO: check if a value exists
print("JPEG Image" in fileDesc.values())

# TODO: remove a single item
del fileDesc["pdf"]
print(f"Dictionary contains {len(fileDesc)} items")

# TODO: clear all  values
fileDesc.clear()
print(f"Dictionary contains {len(fileDesc)} items")

