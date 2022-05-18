thestr = "The quick brown  fox jumps over the lazy awserdtfyuhkjn dog"
alpha1 = "abcdef"
alpha2 = "ABCDEF"

# TODO: getting the string length
# print(len(thestr))

# # TODO: working with substrings
# print(thestr)
# print(thestr.startswith("The"))
# print(thestr.endswith("dog"))
"""hsjacgusdzbdmszbzkmbn, adz.k.n"""
# print(thestr.find("fox"))
# print(thestr[4:9])

# newstr = thestr.replace("fox", "cat")
# print(newstr)

# TODO: string concatenation
strlist = []
for i in range(10):
    strlist.append(str(i))
thestr="".join(strlist)
print(thestr)

# TODO: string interpolation
interp = f"Lower case letters are {alpha1}, uppercase are {alpha2}"
print(interp)

interp2 = f"{len(alpha1)}"
print(interp2)


