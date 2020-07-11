def mergesort(list):
    print("Splitting ", list)
    if len(list) > 1 :
        mid = len(list)//2
        Lmid = list[:mid]
        Rmid = list[mid:]

        mergesort(Lmid)
        mergesort(Rmid)
        i = j = k =0
        while len(Lmid) > i and len(Rmid) > j:
            if Lmid[i] < Rmid[j]:
                list[k] = Lmid[j]
                i = i + 1
            else:
                list[k] = Rmid[j]
                j = j + 1
            k = k + 1
        while i < len(Lmid):
            list[k] = Lmid[i]
            i = i +1
            k = k + 1

        while j < len(Rmid):
            list[k] = Rmid[j]
            j = j + 1
            k = k + 1
    print(list)
list = []
n = int(input(" enter the number of item in the list : "))
for i in range(0, n):
    element = int(input("enter number: "))
    list.append(element)
print(list)
print("sorted list")
print(mergesort(list))