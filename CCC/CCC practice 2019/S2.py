end=""
primes=[]


def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            #print(p)
            primes.append(p)

    
def solve(num, end):
    first=0
    second=0
    decrease=1
    increase=0
    #print(len(primes))
    avg=num*2
    if(num in primes):
        end=end+str(num)+" "+str(num)+"\n"
        return end
    else:
        for i in range(len(primes)):
            if num<primes[i]:
                first=primes[i-decrease]
                second=primes[i]
                while(True):
                    if second+first==avg:
                        break
                    elif second+first>avg: 
                        decrease+=1
                        first=primes[i-decrease]
                    elif second + first<avg:
                        increase+=1
                        second=primes[i+increase]

                    
                
                end = end+str(first)+" "+str(second) +"\n"
                #print(end)
                return end
                #print(str(primes[i])+", "+str(primes[i-1]))
                break


SieveOfEratosthenes(1100000)
sets=int(input())
data=[]

for i in range(sets):
    num=int(input())
    end = solve(num, end)
    #print(end)
end=end[0:-1]
print(end)
#n = 1000000
#num=87363
#print("Following are the prime numbers smaller") 
#print("than or equal to", n) 

def getPrimes(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if prime[p]==True:
            for i in range(p*p, n+1, p):
                prime[i]=False
        p+=1
    for i in range(2,n):
        if prime[p]:
            print(p)