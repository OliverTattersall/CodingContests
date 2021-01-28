import random

def BinSearch(n, lst, count):

    print(lst)

    m=len(lst)

    if m>0:

        if n>lst[m//2]:

            return BinSearch(n, lst[(m//2)+1 : ], count+1)

        elif n<lst[m//2]:

            return BinSearch(n, lst[0 : m//2], count+1)

        else:

            return lst[m//2], count

    else:

        return -1, count


lst=[i for i in range(1000)]
lst.sort()
print(lst)

n=int(input())

print(BinSearch(n, lst, 0))