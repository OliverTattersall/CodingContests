import random
import heapq


a=[[random.randint(0,20),"A"] for _ in range(2)]
print(a)
a[1][1]="B"

heapq.heapify(a)

print(a)


