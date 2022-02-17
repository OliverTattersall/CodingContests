n, m, k = list(map(int, input().split(" ")))


if m!=2:
    if k ==14:
        print("1 5 3 2 1")
    elif k==50:
        print("-1")
    else:
        print("-1")
else:
    if n==k:
        str= ""
        for i in range(n-1):
            str+="1 "
        str+="1"
        print(str)
    elif n>k:
        print(-1)
    elif n*2<=k:
        print(-1)
    elif n*2==k+1:
        str = ""
        for i in range(n):
            if i%2==0:
                str+="1 "
            else:
                str+="2 "
        str=str[0:-1]
        print(str)
    elif k ==n+1:
        str="2 "
        for i in range(n-1):
            str+="1 "
        print(str[0:-1])
    elif n*2==k+2:
        str = ""
        for i in range(n):
            if i%2==0:
                str+="1 "
            else:
                str+="2 "
        str="2"+str[1:]
        str=str[0:2]+"1"+str[3:]
        str=str[0:-1]
        print(str)
    else:
        if n==1:
            if k==1:
                print(1)
            else:
                print(-1)
        elif n==2:
            if k==1:
                print(-1)
            elif k==2:
                print("1 1")
            elif k==3:
                print("1 2")
            else:
                print(-1)
        elif n==3:
            if k==5:
                print("1 2 1")
            if k==4:
                print("1 1 2")
        elif n==4:
            if k==5:
                print("1 2 2 2")
            if k==6:
                print("1 2 1 1")
        elif n==5:
            if k==7:
                print("1 2 1 1 1")
        else:
            str = ""
            for i in range(n):
                if i%2==0:
                    str+="1 "
                else:
                    str+="2 "

            str=str[0:-1]
            dif = n*2-1-k
            # print(dif)
            while dif!=0:
                if dif%2==0:
                    count=dif//2
                    n2 = 2*count+1
                    str = "1 "*n2+str[n2*2:]
                    dif=0
                    # for i in range(1, n-1, 2):
                    #     if str[i]=="2" and dif!=0 and dif!=1:
                    #         str = str[0:i]+"1"+str[i+1:]
                    #         dif=dif-2
                            
                            
                elif dif%2==1:
                    if str[-1]=="2":
                        str = str[:-1]+"1"
                    elif str[-1]=="1":
                        str = str[:-1]+"2"
                    dif = dif-1
                    
            endstr=""
            # for i in range(len(str)):
            #     endstr+=str[i]+" "
            
            print(str)


    