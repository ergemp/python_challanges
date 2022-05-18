ll = [[3,0,0,1,2],
      [0,1,4,0,0],
      [5,0,0,3,3]]


def treasure_finder(gll):
    map_final = []
    row_final = []
    for elem1 in gll:

        if len(elem1) == 0:
            return 0

        row_total = 0
        for elem2 in elem1:
            if elem2 > 0:
                row_total = row_total + elem2
            elif elem2 == 0:
                row_final.append(row_total)
                row_total = 0
            elif elem2 < 0:
                return -1

            row_final.append(row_total)

        map_final.append(max(row_final))
    return max(map_final)


retval = treasure_finder(ll)
print (retval)


