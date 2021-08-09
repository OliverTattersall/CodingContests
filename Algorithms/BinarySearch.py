import random

def BinSearch(n, lst, count, i):

    

    m=len(lst)
    print(m//2, lst[m//2])

    if m>0:

        if n>lst[m//2]:

            return BinSearch(n, lst[(m//2)+1 : ], count+1, i)

        elif n<lst[m//2]:

            return BinSearch(n, lst[0 : m//2], count+1, i)

        elif n==lst[m//2]:

            return lst[m//2], count, i
        else:
            return -1, count

    else:

        return -1, count


lst=[i for i in range(1000)]
lst.sort()
print(lst)

n=int(input())

print(BinSearch(n, lst, 0, 0))