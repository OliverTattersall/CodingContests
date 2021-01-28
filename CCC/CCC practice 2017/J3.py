a,b = input().split(" ")
a=int(a)
b=int(b)
c,d = input().split(" ")
c=int(c)
d=int(d)
charge=int(input())

if (charge - (abs(a-c)+abs(b-d)))>=0:
    if (charge - (abs(a-c)+abs(b-d)))%2==0 :
        print("Y")
    else:
        print("N")
else:
    print("N")
