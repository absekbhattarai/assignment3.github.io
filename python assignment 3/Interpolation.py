def interpolationSearch(list, index):

    (left, right) = (0, len(list) - 1)

    while list[right] != list[left] and list[left] <= index <= list[right]:
        mid = left + (index - list[left]) * (right - left) // (list[right] - list[left])
        if index == list[mid]:
            return mid

        elif index < list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if index == list[left]:
        return left
    return -1


list = []
n = int(input(" enter the number of item in the list : "))
for i in range(0, n):
    element = int(input("enter number: "))
    list.append(element)
key = int(input("enter the key to search for : "))
print(list)
index = interpolationSearch(list, key)

if index != -1:
    print("Element found at index", index)
else:
    print("Element found not in the list")