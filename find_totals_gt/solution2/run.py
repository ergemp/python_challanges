# declaration
from find_totals_gt.solution2.model.result_model import result_model

list = [0,1,2,3,4,5,6,7,8,9]
solution = result_model()

print(list)

index1 = 0
for elem1 in list:
    index1 = index1 + 1
    index2 = 0
    for elem2 in list:
        index2 = index2 + 1
        if (elem1 + elem2) > 10:
            solution.index.append([index1, index2])
            # print(elem1, "+", elem2 , "  is greater than 10")
            # print("index of elements greater than 10 is :", index1, " and ", index2)

solution.print_me();