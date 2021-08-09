import random
import time


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


lst = [random.randint(1, 1000) for i in range(1000000)]
lst2=[random.randint(1, 100) for i in range(2000)]
lst3=[random.randint(1, 100) for i in range(2000)]
# print(lst)
start_time1 = time.time()
heapSort(lst)
print("--- %s seconds ---" % (time.time() - start_time1))
start_time1 = time.time()
heapSort(lst2)
print("--- %s seconds ---" % (time.time() - start_time1))
start_time1 = time.time()
heapSort(lst3)
print("--- %s seconds ---" % (time.time() - start_time1))
# print(lst)