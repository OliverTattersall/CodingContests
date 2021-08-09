def swap(lst, i, j):
    a = lst[i]
    b = lst[j]

    lst[i]=b
    lst[j]=a

    return lst

def selectionSort(lst):
    
    n = len(lst)
    while n!=0:
        for i in range(len(lst)-n, len(lst),1):
            min=float("inf")
            check=0
            if lst[i]<min:
                check=i
                min=lst[i]

        swap(lst, check, len(lst)-n)
        n=n-1
    return lst[::-1]

lst = [64, 34, 25, 12, 22, 11, 90]

print(selectionSort(lst))