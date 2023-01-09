def find2smallests(lst):

    if lst[0]>=lst[1]:
        min2 = ((lst[1], 1), (lst[0], 0))
    else:
        min2 = ((lst[0],0), (lst[1], 1))

    for i in range(2, len(lst)):
        if lst[i]<=min2[0][0]:
            min2 = ((lst[i], i), min2[0])

        elif lst[i]<=min2[1][0]:
            min2 = (min2[0], (lst[i], i))
    return min2


print(find2smallests([1,6,8,3,6,8,3,4,5,2,7]))
