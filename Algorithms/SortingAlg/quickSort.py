import time
import random
# import sys
# sys.setrecursionlimit(1500)


lst=[random.randint(1,1000) for i in range(1000)]
lst2=lst.copy()
# lst=[10, 80, 30, 90, 40, 50, 70]
lst3=[i for i in range(1000)]
lst4=lst3.copy()

def partition(arr, low, high):

    pivot=arr[high]
    i=low-1
    for j in range(low, high, 1):
        if arr[j]<=pivot:
            # swap(arr, j, i)
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    # swap(arr, i+1, high)
    arr[high], arr[i+1] = arr[i+1], arr[high]
    # print(arr)
    return i+1


def quicksort(arr, low, high):
    if low<high:
        p = partition(arr, low, high)

        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

#print(lst2)
start_time1 = time.time()
quicksort(lst,0, len(lst)-1)

#print(lst2)

print("--- %s seconds ---" % (time.time() - start_time1))
# t = time.time()
# quicksort(lst3, 0, len(lst3)-1)
# print("--- %s seconds ---" % (time.time() - t))

# print(lst)






####
#Hoare method
def partition2(arr, lo, hi):
    p = arr[(hi+lo)//2]
    i=lo-1
    j=hi+1
    while True:
        i+=1
        while arr[i]<p:
            i+=1
        j-=1    
        while arr[j]>p:
            j-=1

        if i>=j:
            return j
        arr[i], arr[j] = arr[j],arr[i]



def quicksort2(arr, lo,hi):
    if lo<hi:
        p=partition2(arr, lo, hi)
        quicksort2(arr, lo, p)
        quicksort2(arr, p+1, hi)



start_time2 = time.time()
quicksort2(lst2, 0, len(lst2)-1)
print("--- %s seconds ---" % (time.time() - start_time2))
t2 = time.time()
quicksort2(lst4, 0, len(lst4)-1)
print("--- %s seconds ---" % (time.time() - t2))

# print(lst2)
