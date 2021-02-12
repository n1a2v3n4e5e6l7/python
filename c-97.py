intro = input("Please Enter Your IntroDuction: ")
letterCount = 0
WordCount = 1
for i in intro:
    letterCount = letterCount+1
    if i==' ':
        WordCount = WordCount+1
print ("Number of words in the your introduction: "+str(WordCount) )
print ("number of Letters on your introduction: " +str(letterCount))        