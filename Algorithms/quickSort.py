import time
import random
import sys
sys.setrecursionlimit(1500)
start_time1 = time.time()

lst=[random.randint(1,1000) for i in range(1000000)]
# lst2=[10, 80, 30, 90, 40, 50, 70]

def swap(arr, index1, index2):
    temp1=arr[index1]
    temp2=arr[index2]
    arr[index1]=temp2
    arr[index2]=temp1
    return arr

def partition(arr, low, high):
    # print(arr)
    pivot=arr[high]
    i=low-1
    for j in range(low, high, 1):
        if arr[j]<pivot:
            i+=1
            swap(arr, j, i)
    swap(arr, i+1, high)
    # print(arr)
    return i+1


def quicksort(arr, low, high):
    if low<high:
        p = partition(arr, low, high)

        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

#print(lst2)
quicksort(lst,0, len(lst)-1)

#print(lst2)

print("--- %s seconds ---" % (time.time() - start_time1))