x = int(input())
days=int(input())


if x<2:
    print("Before")
elif x>2:
    print("After")
elif x==2:
    if days<18:
        print("Before")
    elif days>18:
        print("After")
    else:
        print("Special")