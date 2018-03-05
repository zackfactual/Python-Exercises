listA = [67, 45, 2, 13, 1, 998]
listB = [89, 23, 33, 45, 10, 12, 45, 45, 45]

# sorted() returns new sorted list from any iterable
listASorted = sorted(listA)

print(listASorted) # [1, 2, 13, 45, 67, 998]

print(listA) # [67, 45, 2, 13, 1, 998]

# sort() sorts list in place, changing indices; returns none
listA.sort()

print(listA) # [1, 2, 13, 45, 67, 998]

# manual sort
listANewSort = []
while listA:
    minVal = listA[0]
    for item in listA:
        if item < minVal:
            minVal = item
    listANewSort.append(minVal)
    listA.remove(minVal)
print(listANewSort) # [1, 2, 13, 45, 67, 998]

listBNewSort = []
while listB:
    minVal = listB[0]
    for item in listB:
        if item < minVal:
            minVal = item
    listBNewSort.append(minVal)
    listB.remove(minVal)
print(listBNewSort) # [10, 12, 23, 33, 45, 45, 45, 45, 89]
