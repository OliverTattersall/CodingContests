#incomplete


w = int(input())
n = int(input())
nums = list(map(int, input().split(" ")))

def subSet(i, w, nums, lookup, ns, check):
    if w==200 and i==3:
        print(i, (i,w)in lookup)
    if w==150 and i==2:
        print(i, (i,w) in lookup)
    if w==100 and i==1:
        print(i, (i,w) in lookup)
    if sorted(ns) == (25,25, 25,25,50,50,50,50):
            print(i)

        # print(w)
    if w==0:
        temp = tuple(sorted(ns))
        
        if temp not in check:
            check.add(temp)
            print(check)
            return 1
    if w<0:
        return 0

    if i==-1:
        # print(check)
        return 0
    
    key=(i,w)
    if key not in lookup:
        #include
        inc = subSet(i-1, w-nums[i], nums, lookup, ns+(nums[i], ), check)
        #exclude
        exc = subSet(i-1, w, nums, lookup, ns, check)
        lookup[key] = inc+exc
    

    return lookup[key]


print(subSet(n-1, w, nums, {}, tuple(), set()))
