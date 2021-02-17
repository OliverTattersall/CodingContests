n = int(input())

heights = input().split()
widths = input().split()

for i in range(n+1):
    heights[i] = int(heights[i])
    if i<n:
        widths[i] = int(widths[i])

sum = 0

for i in range(n):
    temp = widths[i]*(heights[i]+heights[i+1])/2
    sum+=temp

print(sum)