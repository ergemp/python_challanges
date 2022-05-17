import numpy

random_array = numpy.random.randint(1,10,10)

print(random_array)

index1 = 1
for elem1 in random_array:
    index2 = 1
    for elem2 in random_array:
        if elem1 + elem2 > 10:
            print(elem1, " + ", elem2, " is greater than 10")
            print("positions ", index1 , " ", index2)
        index2 = index2 + 1
    index1 = index1 + 1


