
def linearsearch(list):
    for i in range(len(list)):
        if x== list[i]:
            print("The index is ", i)
    return -1




list = []
n = int(input(" enter the number of item in the list : "))

x = int(input(" enter the number you want to search for : "))
for i in range(0, n):
    element = int(input("enter number: "))
    list.append(element)
print(list)
print(linearsearch(list))