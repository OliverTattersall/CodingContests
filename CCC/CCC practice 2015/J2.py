string=input()
happy=0
sad=0
for i in range(len(string)):
    if i<len(string)-2:
        if string[i]==":":
            if string[i+1]=="-":
                if string[i+2]==")":
                    happy=happy+1
                elif string[i+2]=="(":
                    sad=sad+1
if(happy == 0 and sad == 0):
    print("none")
elif happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif sad == happy:
    print("unsure")