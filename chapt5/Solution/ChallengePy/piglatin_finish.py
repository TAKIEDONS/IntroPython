def topiglatin(sentence):
    vowels = "AEIOUaeiou"
    plword =[]
    curwords = sentence.split(' ')

    for word in curwords:
        # if the word starts with a vowel just append "way" to the word
        if vowels.find(word[0:1]) != -1:
            plword.append(word + "way")

        else:
            # find the position of the fisrt vowel
            for i, c in enumerate(word):
                indx = vowels.find(c)
                if indx != -1:
                    prefix = word[0:1]
                    suffix = word[i:]
                    newword = suffix + prefix + "ay"
                    plword.append(newword)
                    break
       # return all of the words joined into a sentence
    return " ".join(plword)

teststr = input("Enter a string to cpnvert to pigLatin: ")
    
piglatinstr = topiglatin(teststr)
print("The result is: ")
print(piglatinstr)
