def createlist(list1):
    count=int(input("Enter number of elements you want"))
    for i in range(count):
        data=int(input("Enter element"))
        list1.append(data)

def display(list1):
    print("Element in list are:")
    for i in range(len(list1)):
        print(list1[i], " ", end='')
    print('')

if __name__ == '__main__':
    list1=[]
    list2=[]
    createlist(list1)
    createlist(list2)
    display(list1)
    display(list2)