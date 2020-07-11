def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1] :
                list[j] , list[j+1] = list[j+1] , list[j]
            else:
                pass
    return list
list = []
n = int(input(" enter the number of item in the list : "))
for i in range(0, n):
    element = int(input("enter number: "))
    list.append(element)
print("unsorted List")
print(list)
print("sorted list")
print(bubblesort(list))