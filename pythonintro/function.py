def countwordsfromfile():
    filename=input("Enter The file name: ")
    numberofwords=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print("numberofwords: ")
    print(numberofwords)

countwordsfromfile()
