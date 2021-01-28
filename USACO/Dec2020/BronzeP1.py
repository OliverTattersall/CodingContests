nums=input().split(" ")
# nums="2 6 7 4 5 9 11".split()

for i in range(len(nums)):
    nums[i]=int(nums[i])

nums.sort()

# print(nums)

total=nums[-1]


A=nums[0]
B=nums[1]
C=total-A-B

BC=total-A


# rest=nums[1:5]


# minusA=[]
# for i in range(len(rest)):
#     minusA.append(rest[i]-A)
#     if (rest[i]-A)==0:
#         B = rest[i]
# # print(B)

# if B!=0:
#     C=total-A-B










print(A,B,C)