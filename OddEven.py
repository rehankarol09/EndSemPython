def median_fun(list2):
    list1=list2
    n=len(list1)
    list1.sort()
    median=0
    if n % 2 == 0:
        median1=list1[n//2]
        median2=list1[(n-1)//2]
        median=(median1+median2)/2
    else:
        median=list1[n//2]
    return median

def len_array(list1):
    return len(list1)

def createlist_even(list1):
    n=0
    n = int(input("Enter the no of elements in even range"))
    while True:
        if n%2 ==0 and n!=0:
            for i in range(n):
                data = int(input("Enter the element"))
                list1.append(data)
            break
        else:
            n = int(input("Enter the no of elements in even range"))



def createlist_odd(list1):
    n=0
    while True:
        n=int(input("Enter the no of elements in odd range"))
        if n%2!=0 and n!=0:
            for i in range(n):
                data=int(input("Enter the element"))
                list1.append(data)
            break
        else:
            n = int(input("Enter the no of elements in odd range"))



if __name__ == '__main__':
    list1=[]
    createlist_even(list1)
    list2=[]
    createlist_odd(list2)

    print("The median of 1 array:"+ str(median_fun(list1)))
    print("The length of fisrt array:", len_array(list1))
    print("The median of 2 array:" + str(median_fun(list2)))
    print("The length of second array:", len_array(list2))






