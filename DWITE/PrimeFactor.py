import random

n=int(input())

smallprimes=[2,3,5,7,11,13,17,19]


primes=[]

def is_Prime(n):

    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        
        d>>=1
        s+=1

 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):

            if pow(a, 2**i * d, n) == n-1:
                
                return False
        return True  
    nums=set()
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        while a in nums:
            a=random.randrange(2, n)

        nums.add(a)
        result=trial_composite(a)
        if result:
            return False
 
    return True


def PrimeFactor(n):
    for i in range(8):
        if n%smallprimes[i]==0:
            return n//smallprimes[i]

    j=20
    if is_Prime(n):
        return 1
    while j<=(n**(1/2)):

        if n%j==0:
            if is_Prime(j):
                return n//j

        j+=1
    



while n!=1:
    temp=n
    n=PrimeFactor(n)
    primes.append(temp//n)

print(primes)
    
answer=""
for i in range(len(primes)-1):
    answer+=str(primes[i])+"*"

answer+=str(primes[-1])
print(answer)