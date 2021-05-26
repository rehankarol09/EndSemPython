
#----while loops---
#printing even no in range using while
range=int(input("Enter the range till which you want to find even no"))
i=0
evenno=[]
while i<=range:
    if i%2 == 0:
        evenno.append(i)
    i+=1

#---for loops--
#printing odd no in range using for loops
range1=int(input("Enter the range in which you want to find odd no"))
oddno=[]
for i in range(range1+1):
    if i%2!=0:
        oddno.append(i)
print(oddno)


#---Python doesnt support for do while loop
#---alternate is to run one infinite loop and break it
i=0
range= 15
while True:
    if i>range:
        break
    else:
        print(i)
        i+=1


