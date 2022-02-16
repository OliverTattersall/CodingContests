n = int(input())
heights = input().split(" ")
widths = input().split(" ")

sum = 0
for i in range(n):
    sum += ((int(heights[i])+int(heights[i+1]))/2)*int(widths[i])

print(sum)

