# primes= [2,3,5,7,11,13,17,19, 23]
# def primefactor(n):

#     if n==1:
#         return ()

#     i=0
#     while primes[i]<=n:
#         if n%primes[i]==0:
#             return primefactor(n//primes[i])+(primes[i], )
#         i+=1
# # print(primefactor(8))


# primefactors=[]

# for i in range(2, 21, 1):
#     primefactors.append(primefactor(i))

# print(primefactors)


# end = {}

# for i in range(len(primefactors)):
#     temp={}
#     for j in range(len(primefactors[i])):
#         temp[primefactors[i][j]]= temp.get(primefactors[i][j], 0)+1
    


####
# Way 2

####

def gcd(a,b):
    if a==0 or b==0:
        return a+b  
    r=a%b
    a=b
    b=r
    return gcd(a,b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

prod=2
for i in range(3, 21, 1):
    prod = lcm(prod, i)
print(prod)
