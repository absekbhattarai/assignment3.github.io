def insertionsort(list):
    for i in range(1,len(list)):
        currentvalue = list[i]
        currentposition = i
        while currentposition > 0 and list[currentposition -1 ] > currentvalue:
            list[currentposition] = list[currentposition - 1]
            currentposition = currentposition -1
        list[currentposition] = currentvalue
    return list
list = []
n = int(input(" enter the number of item in the list : "))
for i in range(0, n):
    element = int(input("enter number: "))
    list.append(element)
print("unsorted List")
print(list)
print("sorted list")
print(insertionsort(list))