def binarysearch(lst, num):
            below=0
            above=0
            
            low = 0
            high = len(lst)
            while low<=high:
                med = (high+low)//2
                # print(med)
                if lst[med]==num:
                    below = med 
                    above = len(lst)-med-1
                    break
                elif lst[med]>num:
                    high = med-1
                else:
                    low = med+1
            
            if below ==0 and above ==0:
                
                med = (high+low)/2
                # print(med, high, low)
                below = int(med)+1
                above = len(lst)-int(med)-1
                
                
            return below,above

def findMedianSortedArrays(nums1, nums2):
    med = nums1[(len(nums1)-1)//2]
    below1 = (len(nums1)-1)//2
    above1 = len(nums1)-below1-1

    below2, above2 = binarysearch(nums2, med)
    while abs((below1+below2)-(above1+above2))>2:
            if (below1+below2)<(above1+above2):

                pass

print(binarysearch([0,1,3,3.5,4,5,6,7], 3.5))


# [1,2,3,4]
# [5,6,7]

# [1,2,3,4,5,6,7]
'''

2.5
6
'''