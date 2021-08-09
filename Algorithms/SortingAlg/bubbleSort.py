##homemade bubble sort
def swap(lst, i, j):
    a = lst[i]
    b = lst[j]

    lst[i]=b
    lst[j]=a

    return lst

def Bubblesort(lst):
    switches=1
    while switches!=0:
        switches=0
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                switches+=1
                lst = swap(lst, i, i+1)

    return lst
lst = [64, 34, 25, 12, 22, 11, 90]
print(Bubblesort(lst))