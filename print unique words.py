file1=input("Enter file name")
uniquewords=[]
with open(file1, 'r') as file:
    for line in file:
        for words in line.split():
            if words not in uniquewords:
                uniquewords.append(words)
for i in range(len(uniquewords)):
    print(uniquewords[i])

