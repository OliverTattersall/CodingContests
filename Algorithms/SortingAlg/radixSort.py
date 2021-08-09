import time
import random
import sys
start_time1 = time.time()

def countingSort(arr, exp1): 
    # print(exp1)
    # print(arr)
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i] / exp1) 
        count[int(index % 10)] += 1
  
    # Change count[i] so that count[i] now contains actual 
    # position of this digit in output array 
    for i in range(1, 10): 
        count[i] += count[i - 1] 
  
    # Build the output array 
    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0, len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def radixSort(arr): 
    count=0
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
    # print(max1)
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1 // exp > 0: 
        count+=1
        countingSort(arr, exp) 
        exp *= 10
    # print(count)
  
  
# Driver code 
arr = [random.randint(1,1000) for i in range(1000000)]
  
# Function Call 
radixSort(arr) 
  
# for i in range(len(arr)): 
#     print(arr[i]) 
# print(arr)

print("--- %s seconds ---" % (time.time() - start_time1))