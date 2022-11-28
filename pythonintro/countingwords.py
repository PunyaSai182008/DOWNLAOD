intro=input("Enter Your Introduction")
charactercounts=0
wordcounts=1
for i in intro:
    charactercounts=charactercounts+1
    if(i==" "):
        wordcounts=wordcounts+1
print("Number of words in the string: ")
print(wordcounts)
print("Number of character in the string: ")
print(charactercounts)
