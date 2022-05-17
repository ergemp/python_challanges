# declaration
list = [0,1,2,3,4,5,6,7,8,9]


print(list)

index1 = 0
for elem1 in list:
    index1 = index1 + 1
    index2 = 0
    for elem2 in list:
        index2 = index2 + 1
        if (elem1 + elem2) > 10:
            print(elem1, "+", elem2 , "  is greater than 10")
            print("index of elements greater than 10 is :", index1, " and ", index2)

