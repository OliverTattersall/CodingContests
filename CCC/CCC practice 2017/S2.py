N=int(input())
measurements=input().split(" ")

for i in range(len(measurements)):
    measurements[i]=int(measurements[i])
measurements.sort()
discarded=None
#print(measurements)
if len(measurements)%2==1:
    discarded=measurements[int(len(measurements)/2-0.5)]
    measurements.pop(int(len(measurements)/2-0.5))
front=measurements[0:int(len(measurements)/2)]
end=measurements[int(len(measurements)/2):]
front=front[::-1]

# print(front)
# print(end)

# print(discarded)

endstr=""


if discarded!=None:
    endstr=str(discarded)+" "

    for i in range(N - 1):

        if i%2==0:
            endstr+= str(end[i//2]) + " "

        else:
            
            endstr+= str(front[(i-1)//2]) + " "

else:

    for i in range(N):

        if i%2==0:
            endstr+= str(front[i//2]) + " "

        else:
            
            endstr+= str(end[(i-1)//2]) + " "



print(endstr)