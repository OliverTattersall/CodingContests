primes=[]


def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    print(len(prime))
    p = 2
    #goes until √n at which point there would be no more composite numbers left True
    while (p * p <= n): 
        #print(prime[p])
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
    #print(primes)
    #print(len(primes))



n = 1000000
print("Following are the prime numbers smaller") 
print("than or equal to", n) 
SieveOfEratosthenes(n)

