def createlist(list1):
    count=int(input("Enter number of elements you want"))
    for i in range(count):
        data=int(input("Enter element"))
        list1.append(data)

def display(list1):
    for i in range(len(list1)):
        print(list1[i], " ", end='')

if __name__ == '__main__':
    list1=[]*10
    createlist(list1)
    display(list1)

