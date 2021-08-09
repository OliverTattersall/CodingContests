
'''
This function takes integer n and t and returns the highest product formed by t consecutive digits in n
Parameters: Integer n, Integer t
Conditions: n>0, 0<t<n
'''

def EulerProblem8(n, t):
    product=0
    n=str(n)
    possibilities=[]
    
    #this while removes the digits not available because they would have a 0 in their product
    while n.count("0")!=0:
        # print(len(n)) # all print functions inside this function are used as testing methods to see the process
        index=n.find("0")
        # print(index)
        ind=n.find("0", index+1)
        # print(ind)
        if index<=t:
            
            # ind=n.find("0", index+1)
            if ind-index<=13 and ind!=-1:
                # print(True)
                # print(n[0:ind])
                n=n[ind:]
            else:
                n=n[index+1:]
        elif index>t and ind!=-1:
            possibilities.append(n[0:index])
            # ind=n.find("0", index+1)
            if ind-index<=13:
                n=n[ind-1:]
            else:
                n=n[index+1:]
            
        elif index<=t and ind==-1:
            if len(n)-index<=t:
                n=""
            else:
                n=n[index+1:]
            
        elif index>t and ind==-1:
            possibilities.append(n[0:index])
            if len(n)-index<=t:
                n=n[0:index]
            else:
                possibilities.append(n[index+1:])
                n=""
    

    print(possibilities)#list full of groups of numbers that can be searched through 

    #for loop that looks through each item in possibilities 
    for h in range(len(possibilities)):
        
        #for loop that goes through every consequitive 13 digits in possibilities[h]
        for i in range(len(possibilities[h])-t+1):
            temp=possibilities[h][i:i+t]

            temp2=1
            #for loop that goes through every digit and multiplies it to a temp value to get the product of the 13 digits
            for j in range(len(temp)):
                temp2=temp2*int(temp[j])
                # print(temp2)
            if temp2>product:
                    product=temp2

    return product

# print(EulerProblem8(137097548548573920034672842032487, 7))
print(EulerProblem8(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450,13))

